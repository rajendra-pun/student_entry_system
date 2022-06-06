from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=5)
    address = models.CharField(max_length=100)
    grade = models.IntegerField(default=1)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.name