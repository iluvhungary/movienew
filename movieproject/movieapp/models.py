from django.db import models

# Create your models here.
#I need a table for my movie project with name,description and year
class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

