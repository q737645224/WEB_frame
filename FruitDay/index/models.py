from django.db import models

# Create your models here.
class User(models.Model):
  uphone=models.CharField(max_length=11)
  upwd=models.CharField(max_length=20)
  uname=models.CharField(max_length=30)
  uemail=models.EmailField()
  isActive=models.BooleanField(default=True)

  def __str__(self):
    return self.uname

  class Meta:
    db_table = 'user'
