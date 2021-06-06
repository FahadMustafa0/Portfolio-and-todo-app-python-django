from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    msg=models.TextField(max_length=122)
    def __str__(self):
      return self.name   
class todo(models.Model):
  date=models.DateTimeField()
  text=models.CharField(max_length=200)
  def __str__(self):
      return self.text




