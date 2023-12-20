# forms.py
from django import forms
from .models import Participant, Vehicles
from django import forms
from django.forms import formset_factory

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Enter your middle name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'reference_number': forms.TextInput(attrs={'placeholder': 'Enter your reference number'}),
            'gender': forms.Select(attrs={'placeholder': 'Select your gender'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = ['plates', 'make', 'color', 'man_date', 'car_type', 'participant']
        widgets = {
            'plates': forms.TextInput(attrs={'placeholder': 'Enter license plate number'}),
            'make': forms.TextInput(attrs={'placeholder': 'Enter vehicle make'}),
            'color': forms.TextInput(attrs={'placeholder': 'Enter vehicle color'}),
            'man_date': forms.DateInput(attrs={'placeholder': 'Enter manufacture year'}),
            'participant': forms.Select(attrs={'class': 'placeholder'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant'].queryset = Participant.objects.all()




