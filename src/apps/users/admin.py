from django.contrib import admin

from src.apps.users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "rang",)
    search_fields = ("username", "email",)
