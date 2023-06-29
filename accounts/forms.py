from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'email']


class LoginForm(AuthenticationForm):
    pass


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='이름')  # 이름
    last_name = forms.CharField(max_length=30, required=True, label='성')  # 성

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('last_name', 'first_name',)
