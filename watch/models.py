from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    address = models.CharField(max_length=50)


class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    stock=models.IntegerField()
    category=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)

    verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
