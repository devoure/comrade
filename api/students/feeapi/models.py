from django.db import models
from django.conf import settings

# Create your models here.

class Fee(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    reg_number = models.CharField(max_length=20)
    fee_balance = models.CharField(max_length=10)
    cleared = models.BooleanField(default=False)
    def __str__(self):
        return self.reg_number

