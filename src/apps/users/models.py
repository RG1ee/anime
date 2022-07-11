from django.db import models

from django.contrib.auth.models import AbstractUser
from apps.achievements.models import Achievement

from apps.users.const import RangUser
from apps.users.signals import add_welcome_achievement


class User(AbstractUser):
    rang = models.PositiveSmallIntegerField(
        choices=RangUser.choices, verbose_name='User Rang',
        default=RangUser.STUDENT_OF_THЕ_ACADEMY
    )
    achievement = models.ManyToManyField(Achievement)


models.signals.post_save.connect(add_welcome_achievement, User)
