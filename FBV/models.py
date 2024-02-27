from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    uid=models.IntegerField()
    address=models.TextField()