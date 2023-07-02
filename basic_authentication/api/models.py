from django.db import models

# Create your models here.
class Student_model(models.Model):
    student_name = models.CharField(max_length=100)
    student_roll = models.IntegerField()
    present_city = models.CharField(max_length=100)
