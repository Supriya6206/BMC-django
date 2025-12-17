from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=40)
    
    def _str_(self):
        return self.name