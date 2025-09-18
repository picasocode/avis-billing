# business/views.py
from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BusinessProfile

def setup_business_view(request):
    """Render Business Setup HTML Form"""
    return render(request, "business/setup.html", {"now": now()})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def setup_business_profile(request):
    """
    API: Save business details after first login (must be authenticated)
    """
    owner = request.user

    # If profile exists, return error
    if hasattr(owner, "business_profile"):
        return Response({"error": "Business profile already exists"}, status=400)

    data = request.data
    required_fields = ["business_name", "phone_number"]
    for f in required_fields:
        if not data.get(f):
            return Response({"error": f"{f} is required"}, status=400)

    profile = BusinessProfile.objects.create(
        owner=owner,
        business_name=data.get("business_name"),
        phone_number=data.get("phone_number"),
        gst_number=data.get("gst_number"),
        billing_address=data.get("billing_address"),
        bank_name=data.get("bank_name"),
        account_number=data.get("account_number"),
        ifsc_code=data.get("ifsc_code"),
    )

    return Response({
        "message": "Business profile created successfully",
        "profile": {
            "id": profile.id,
            "business_name": profile.business_name,
            "phone_number": profile.phone_number,
            "gst_number": profile.gst_number,
            "billing_address": profile.billing_address
        }
    })
