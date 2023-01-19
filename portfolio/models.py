from django.db import models

# Create your models here. Cioè una classe per rappresentare il progetto
# bisogna essere un po piu specifici con la django
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    

    def __str__(self):
        return self.title
