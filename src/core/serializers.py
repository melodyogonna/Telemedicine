from rest_framework import serializers

from core.models import Appointments

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        """Serializer for the appointment model"""
        model = Appointments
        fields = '_all_'
