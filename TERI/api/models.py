from django.db import models
from django.contrib.auth.models import User , AbstractUser

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)


class Negocios(models.Model):
    name=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    foundation=models.PositiveBigIntegerField()