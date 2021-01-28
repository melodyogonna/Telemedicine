from rest_framework import serializers

from core.models import Appointments, BlockedDays


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        """Serializer for the appointment model"""

        model = Appointments
        fields = "__all__"


class BlockedDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedDays
        fields = "__all__"
