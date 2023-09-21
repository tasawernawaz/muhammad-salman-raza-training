from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

from .models import UserProfile


@receiver(post_save, sender=UserProfile)
def user_profile(sender, instance, created, **kwargs):
    if created:
        today = datetime.today()
        age = (
            today.year
            - instance.date_of_birth.year
            - (
                (today.month, today.day)
                < (instance.date_of_birth.month, instance.date_of_birth.day)
            )
        )
        instance.age = age
        instance.save()

        subject = "Welcome to our website"
        message = "Thank you for signing up at our Website. We are excited to have you as a member!"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            print(f"Email sending failed: {e}")
