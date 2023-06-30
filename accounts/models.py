from django.conf import settings
from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.urls import reverse

phone_regex = RegexValidator(
        regex=r'^\d{3}-\d{4}-\d{4}$',
        message='전화번호는 010-0000-0000 형식이어야 합니다.'
    )

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='유저')

    phone_number = models.CharField(
        max_length=13,
        validators=[phone_regex],
        verbose_name='전화번호',
    )
