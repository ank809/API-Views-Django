from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    course=models.CharField(max_length=50)
    reg_no=models.IntegerField()