from django.core.exceptions import ValidationError
from django.utils import timezone


# Custom validator for date_of_birth
def validate_date_of_birth(value):
    if value and value > timezone.now().date():
        raise ValidationError("Date of birth cannot be in the future")
