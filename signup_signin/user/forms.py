from django import forms
from .models import UserProfile

class UserRegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserProfile
        fields = ['city', 'country', 'date_of_birth', 'full_name', 'username', 'password']

    def clean_username(self):
        instance = self.instance
        username = self.cleaned_data.get('username')
        qs = UserProfile.objects.filter(username__iexact = username)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError('This username is already taken :(')
        return username

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
