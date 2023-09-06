from django import forms
from .models import UserProfile

class UserRegisterationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['city', 'country', 'date_of_birth', 'full_name', 'username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = UserProfile.objects.filter(username__iexact = username).exists()
        if qs:
            raise forms.ValidationError('This username is already taken :(')
        return username

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
