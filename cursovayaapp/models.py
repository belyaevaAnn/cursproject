from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    number = models.CharField(max_length=11)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=300, default='')
    privilegies = models.BooleanField(default=0)


class Material(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    imag = models.ImageField(upload_to="static/images", blank=True)


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    type = models.BooleanField(default=0)


class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_number = models.CharField(max_length=11)
    description = models.TextField(default=' ')
    time = models.DateField(default=timezone.now)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
    master_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service_id = models.ManyToManyField(Service)
    materail_id = models.ManyToManyField(Material)
    count_material = models.IntegerField(default=0)


class Review(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
