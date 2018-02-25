from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    #image = models.ImageField()
    name = models.TextField(max_length=100)
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    #categories = models.TextField()

    def __str__(self):
        return self.name
