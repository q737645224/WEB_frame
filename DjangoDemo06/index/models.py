from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  email = models.EmailField()
  isActive = models.BooleanField(default=True)

  def to_dict(self):
    dic = {
      'id':self.id,
      'name':self.name,
      'age':self.age,
      'email':self.email,
      'isActive':self.isActive,
    }
    return dic

  class Meta:
    db_table = 'author'