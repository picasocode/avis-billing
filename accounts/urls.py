from django.urls import path
from .views import (
    superadmin_login_view,
    otp_login_view,
    superadmin_login,
    send_otp,
    verify_otp,
)

app_name = "accounts"

urlpatterns = [
    # ----------------
    # UI Pages
    # ----------------
    path("superadmin-login/", superadmin_login_view, name="superadmin-login"),
    path("otp-login/", otp_login_view, name="otp-login"),

    # ----------------
    # API Endpoints
    # ----------------
    path("api/superadmin-login/", superadmin_login, name="api-superadmin-login"),
    path("api/send-otp/", send_otp, name="api-send-otp"),
    path("api/verify-otp/", verify_otp, name="api-verify-otp"),
]
