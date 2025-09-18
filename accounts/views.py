# accounts/views.py
import random
from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# ---------- Template Views ----------
def superadmin_login_view(request):
    """Render SuperAdmin login page (email + password)."""
    return render(request, "accounts/superadmin_login.html", {"now": now()})

def otp_login_view(request):
    """Render OTP login page (Shop Owner / Staff)."""
    return render(request, "accounts/otp_login.html", {"now": now()})


# ---------- Temporary OTP store (dev only) ----------
# NOTE: In production use Redis or cache backend
otp_store = {}


# ---------- API Endpoints ----------

@api_view(["POST"])
@permission_classes([AllowAny])
def superadmin_login(request):
    """
    SaaS SuperAdmin logs in with email + password (API).
    Expects { "email": "...", "password": "..." }.
    """
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=400)

    # authenticate uses USERNAME_FIELD. If you use email as username, ensure that works.
    user = authenticate(username=email, password=password)

    if not user:
        return Response({"error": "Invalid credentials"}, status=401)

    if not getattr(user, "is_superadmin", False):
        return Response({"error": "Not authorized as SuperAdmin"}, status=403)

    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "email": user.email,
            "is_superadmin": user.is_superadmin,
        }
    })


@api_view(["POST"])
@permission_classes([AllowAny])
def send_otp(request):
    """
    Generates a 6-digit OTP for phone number login
    """
    phone = request.data.get("phone")
    if not phone:
        return Response({"error": "Phone is required"}, status=400)

    otp = str(random.randint(100000, 999999))
    otp_store[phone] = otp

    # TODO: Replace with Twilio / Firebase SMS integration in production
    print(f"[DEBUG] OTP for {phone}: {otp}")

    return Response({"message": f"OTP sent to {phone}"})


@api_view(["POST"])
@permission_classes([AllowAny])
def verify_otp(request):
    """
    Verifies OTP and issues JWT tokens. If onboarding required, returns needs_setup + redirect_url.
    """
    phone = request.data.get("phone")
    otp = request.data.get("otp")

    if not phone or not otp:
        return Response({"error": "Phone and OTP are required"}, status=400)

    if otp_store.get(phone) != otp:
        return Response({"error": "Invalid OTP"}, status=400)

    # Create or fetch user. default new users to role 'owner'
    user, created = User.objects.get_or_create(
        phone=phone,
        defaults={"username": phone, "role": "owner"}
    )

    # Consume OTP once used
    otp_store.pop(phone, None)

    # Determine if onboarding is needed. Adjust check to match your business model name.
    needs_setup = True
    try:
        needs_setup = not hasattr(user, "business_profile")
    except Exception:
        # fallback conservative behaviour
        needs_setup = created

    # redirect targets (frontend routes)
    setup_url = "/business/setup-form/"
    dashboard_url = "/dashboard/"
    redirect_url = setup_url if needs_setup else dashboard_url

    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "phone": user.phone,
            "role": user.role,
            "is_superadmin": getattr(user, "is_superadmin", False),
        },
        "needs_setup": needs_setup,
        "redirect_url": redirect_url
    })
