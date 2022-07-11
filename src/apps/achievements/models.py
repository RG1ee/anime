from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
