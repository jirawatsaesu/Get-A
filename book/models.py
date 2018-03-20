from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Categories(models.Model):
    name = models.TextField(max_length=20, default=None)

    def __str__(self):
        return self.name

class Book(models.Model):
    #image = models.ImageField()
    name = models.TextField(max_length=100)
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    categories = models.ForeignKey(Categories, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
