from django.db import models

# Create your models here.
class Person(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    address=models.TextField()
    gender=models.CharField(
        max_length=5,
        choices=[('ชาย','ชาย'),('หญิง','หญิง')],
        default='ชาย'
    )