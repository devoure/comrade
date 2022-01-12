from django.db import models
from django.conf import settings

# Create your models here.

class Exam(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    reg_number = models.CharField(max_length=20)
    grade = models.CharField(max_length=1)
    unit_title = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    remark = models.CharField(max_length=100)
    def __str__(self):
        return self.reg_number

