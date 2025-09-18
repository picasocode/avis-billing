from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_superadmin = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=[("owner", "Owner"), ("staff", "Staff")],
        default="owner"
    )
    business = models.ForeignKey(
        "companies.Business",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email if self.email else self.phone
