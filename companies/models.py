from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    upi_id = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
