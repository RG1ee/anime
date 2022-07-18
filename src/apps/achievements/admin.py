from django.contrib import admin

from apps.achievements.models import Achievement


@admin.register(Achievement)
class Achievement(admin.ModelAdmin):
    list_display = ("__str__",)
