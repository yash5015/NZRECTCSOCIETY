from django.db import models
from django.core import validators
# Create your models here.


class Branch(models.Model):
    bname = models.CharField(max_length=100, blank=False)
    bfiles = models.FileField(upload_to="", blank=False)

    def __str__(self):
        return self.bname


class Loanform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phno = models.CharField(
        validators=[validators.MinLengthValidator(10)], max_length=11, blank=False)
    regno = models.CharField(max_length=25, blank=False)
    userform = models.FileField(upload_to="", blank=False)

    def __str__(self):
        return self.regno
