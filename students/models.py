from django.db import models

# Create your models here.


class StudentsModel(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    degree = models.CharField(max_length=100)
    course = models.CharField(max_length=100)