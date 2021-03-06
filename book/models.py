from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Categories(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.TextField(max_length=100)
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name
