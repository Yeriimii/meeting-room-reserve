from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'phone_number']
    list_display_links = ['user']
    list_filter = ['user']
    search_fields = ['user', 'phone_number']
