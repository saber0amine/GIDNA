from django import forms
from .models import CalendarEntry

class CalendarEntryForm(forms.ModelForm):
    class Meta:
        model = CalendarEntry
        fields = ['date', 'working_mode', 'project_name', 'location']
