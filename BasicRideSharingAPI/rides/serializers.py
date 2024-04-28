from rest_framework import serializers
from .models import Ride
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class RideSerializer(serializers.ModelSerializer):
    rider = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(type='rider'))
    driver = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(type='driver'))

    class Meta:
        model = Ride
        fields = ['id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at']

class RideIdSerializer(serializers.Serializer):
    id = serializers.CharField()

class RideStatusUpdateSerializer(serializers.Serializer):
    STATUS_CHOICES = (
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    ride_id = serializers.CharField()
    new_status = serializers.ChoiceField(choices=STATUS_CHOICES)