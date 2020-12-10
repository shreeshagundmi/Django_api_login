from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()




