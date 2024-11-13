from django import forms
from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['subject', 'day_of_week', 'start_time', 'end_time']
