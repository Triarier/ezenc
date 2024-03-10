# Create your models here.
from django.db import models


class Creature(models.Model):
    name = models.TextField()
    description = models.TextField()
    hit_points = models.IntegerField()
    hit_dice = models.TextField(null=True)
    armor_class = models.TextField()
    speed = models.TextField()
