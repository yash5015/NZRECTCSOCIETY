from django.db import models

# Create your models here.

class Branch(models.Model):
    bname=models.CharField(max_length=100,blank=False)
    bfiles=models.FileField(upload_to="")

    def __str__(self):
        return self.bname