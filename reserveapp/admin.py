from django.contrib import admin
from .models import Room, ReservedRoom


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ['id', 'floor', 'name', 'max_capacity']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ReservedRoom)
class ReservedRoomAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'room', 'reserved_date', 'started_at', 'finished_at', 'created_at']
    list_display_links = ['reserved_date']
    list_filter = ['created_at', 'reserved_date', 'started_at', 'finished_at']
    search_fields = ['room']
