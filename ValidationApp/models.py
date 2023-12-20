# ValidationApp/models.py
import datetime
from logging import Manager
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone


class Participant(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+\d{1,}$', message='Phone number must start with +(code)')])
    reference_number = models.IntegerField(validators=[MinValueValidator(99), MaxValueValidator(999)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(validators=[RegexValidator(regex=r'.*\.ur\.ac\.rw$', message='Email must end with ur.ac.rw')])
    date_of_birth = models.DateField()

    def clean(self):
        if self.date_of_birth is not None:
            # Additional validation rules
            today = timezone.now().date()
            
            if self.date_of_birth > today:
                raise ValidationError("Date of birth cannot be in the future.")

            age = (today - self.date_of_birth).days // 365
            if age < 18:
                raise ValidationError("Participants must be 18 years or older.")
    def __str__(self):
        return f"{self.last_name}   {self.first_name}"
       
            

    
class ManufacturedDate(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            man_date__lte=(datetime.now().date() - timedelta(days=365.25 * 18)),
            email_regex=r'^[a-zA-Z0-9.%+-]+@ur.ac.rw$',
        )
class Vehicles(models.Model):
    def validate_manufact_year_2000(value):
        if value.year < 2000:
            raise ValidationError(('Date must not be older than 2000'))

    plate_regex = RegexValidator(
         regex=r'^((R[A-Z][A-H]\d{1,3}[A-Z])|(RNP\d{1,3}[A-Z])|(RDF\d{1,3}[A-Z])) |(CD\d{1,3}[A-Z])) |(IT\d{1,3}[A-Z])) |(GR\d{1,3}[A-Z]))$',
        message="Plate number must be in correct form"
    )
    
    TYPES_CHOICES = [
        ('p', 'personal'),
        ('non', 'non_personal'),
        ('O', 'Other'),
    ]
    
    plates = models.CharField(max_length=7, validators=[plate_regex])
    make = models.CharField(max_length=255)
    color = models.CharField(max_length=15)
    man_date= models.DateField(validators=[validate_manufact_year_2000])
    car_type = models.CharField(max_length=12, choices=TYPES_CHOICES) 
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='vehicles', null=True, blank=True)
objects = ManufacturedDate()