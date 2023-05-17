from django.db import models

# Create your models here.
class Student(models.Model):#Create model
    matricula = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=30)    
    age = models.IntegerField()