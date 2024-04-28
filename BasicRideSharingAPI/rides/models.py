from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Ride(models.Model):
    STATUS_CHOICES = (
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    rider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='rides_as_rider')
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
