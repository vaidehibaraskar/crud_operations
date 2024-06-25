from django.db import models

# Create your models here.
class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/',default=None)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.TextField(default=None)
