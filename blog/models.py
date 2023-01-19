from django.db import models

# Create your models here.

class Bloggo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateField()

    def __str__(self):
        return self.title