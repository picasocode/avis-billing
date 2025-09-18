from django.urls import path
from .views import setup_business_view, setup_business_profile

app_name = "business"

urlpatterns = [
    # HTML Page
    path("setup-form/", setup_business_view, name="setup-business-form"),

    # API
    path("setup/", setup_business_profile, name="setup-business"),
]
