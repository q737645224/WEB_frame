from django.db import models

# Create your models here.
class User(models.Model):
  uphone=models.CharField(max_length=30)
  upwd=models.CharField(max_length=30)
  uname=models.CharField(max_length=50)
  uemail = models.EmailField()