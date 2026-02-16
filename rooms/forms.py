from django import forms
from django.utils import timezone

from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["title", "description", "start_at", "end_at"]
        widgets = {
            "start_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get("start_at")
        end = cleaned_data.get("end_at")

        if start and start < timezone.now():
            self.add_error(
                "start_at",
                "Reservation cannot start in the past."
            )

        if start and end and start >= end:
            self.add_error(
                "end_at",
                "End time must be after start time."
            )

        return cleaned_data