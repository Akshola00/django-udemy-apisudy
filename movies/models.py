from django.db import models

# Create your models here.
class Moviedata(models.Model):

    name= models.CharField(max_length=200)
    typ = models.CharField(max_length=100, default='action')
    duration= models.FloatField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='images/', default='images/None/NoImg.png')

    def __str__(self):
        return self.name