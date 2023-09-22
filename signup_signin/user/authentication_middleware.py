from datetime import date
from django.shortcuts import redirect
from django.urls import reverse
from datetime import date, datetime
from django.core.exceptions import ValidationError


class AgeRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse("signup"):
            date_of_birth_str = request.POST.get("date_of_birth")
            if date_of_birth_str:
                date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
                if date_of_birth:
                    today = date.today()
                    age = (
                        today.year
                        - date_of_birth.year
                        - (
                            (today.month, today.day)
                            < (date_of_birth.month, date_of_birth.day)
                        )
                    )
                    if age < 18:
                        raise ValidationError(
                            "You must be over 18 to access this website"
                        )

        response = self.get_response(request)
        return response
