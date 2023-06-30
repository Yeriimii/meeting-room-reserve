from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']


class LoginForm(AuthenticationForm):
    pass


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='이름')  # 이름
    last_name = forms.CharField(max_length=30, required=True, label='성')  # 성
    email = forms.EmailField(max_length=254, help_text='이메일 주소를 입력해주세요.')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('last_name', 'first_name', 'email')
