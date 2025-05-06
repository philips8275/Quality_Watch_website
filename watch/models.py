from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    address = models.CharField(max_length=50)
