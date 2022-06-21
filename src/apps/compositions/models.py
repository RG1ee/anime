from django.db import models


class Composition(models.Model):
    name = models.CharField(max_length=120)
    discription = models.TextField()
