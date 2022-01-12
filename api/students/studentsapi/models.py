from django.db import models
from django.conf import settings

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    reg_number = models.CharField(max_length=20)
    course = models.CharField(max_length = 20)
    secret_key = models.CharField(max_length = 20)
    current_semester = models.CharField(max_length=1)
    current_year = models.CharField(max_length=4)
    date_joined = models.DateField()

    def __str__(self):
        return self.reg_number

