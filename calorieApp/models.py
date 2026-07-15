from django.db import models


# Create your models here.

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_calories = models.FloatField()

    def __str__(self):
        return f"{self.food_name}"
