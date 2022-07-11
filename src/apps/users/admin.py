from django.contrib import admin

from apps.users.models import User


class CustomUserAdmin(User):
    pass

admin.site.register(User)
