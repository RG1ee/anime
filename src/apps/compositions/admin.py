from django.contrib import admin
from apps.compositions.models import Composition


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
