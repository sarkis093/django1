from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=9)
    stock = models.IntegerField('stock')

    # def __str__(cls):
    #     return cls.name

class Client(models.Model):
    name  = models.CharField('name', max_length=100)
    surname = models.CharField('surname', max_length=100)
    email = models.EmailField('email', max_length=100)

    # def __str__(cls):
    #     return f'{cls.name} {cls.surname}'