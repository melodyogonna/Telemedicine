from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()

# Create your models here.
class Appointments(models.Model):
    """Table to hold doctor's appointments"""

    patient = models.ForeignKey(USER, related_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(USER, related_name="doctor", on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)


class BlockedDays(models.Model):
    doctor = models.ForeignKey(
        USER, related_name="doctor_blocked_day", on_delete=models.CASCADE
    )
    blocked_day = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
