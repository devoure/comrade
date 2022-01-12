from django.db import models
from django.conf import settings

# Create your models here.

class Enrol(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    reg_number = models.CharField(max_length=20)
    enrol_status = models.BooleanField(default=False)
    semester = models.CharField(max_length=10)
    def __str__(self):
        return self.reg_number

