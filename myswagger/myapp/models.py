from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
