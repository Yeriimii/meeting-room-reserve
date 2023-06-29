from django import forms
from django.forms import Select
from .models import ReservedRoom


class ReservedRoomForm(forms.ModelForm):
    class Meta:
        model = ReservedRoom
        fields = ['room', 'reserved_date', 'started_at', 'finished_at']
        widgets = {
            'reserved_date': forms.DateInput(attrs={'type': 'date'}),
            'started_at': forms.TimeInput(attrs={'type': 'time'}),
            'finished_at': forms.TimeInput(attrs={'type': 'time'}),
        }
