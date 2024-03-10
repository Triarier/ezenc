# Create your models here.
from django.db import models


class Creature(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    hit_points = models.IntegerField()
    hit_dice = models.TextField(null=True)
    armor_class = models.TextField()
    speed = models.TextField()

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nHit Points: {self.hit_points}\nHit Dice: {self.hit_dice}\nArmor Class: {self.armor_class}\nSpeed: {self.speed}"

    class Meta:
        ordering = ["name"]
