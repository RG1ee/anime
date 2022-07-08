from django.db import models


class AnimeStatus(models.IntegerChoices):
    ONGOING = 1, 'Ongoing'
    CAME_OUT = 2, 'Came Out'
    ANNOUNCEMENT = 3, 'Announcement'
