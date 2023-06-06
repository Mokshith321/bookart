from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):
  # id = int
  img = models.ImageField(upload_to='images')
  title = models.CharField(max_length=100)
  cost = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
