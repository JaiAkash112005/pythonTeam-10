from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10)

class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    bookingDate = models.DateField()
    timeSlot = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
