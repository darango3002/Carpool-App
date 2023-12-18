from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from address.models import AddressField

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.name    

class Ride(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start = AddressField(null=True, related_name="start_address")
    destination = AddressField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_departure = models.DateTimeField()
    seats = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.creator.username}\'s Ride'

    def get_absolute_url(self):
        return reverse('ride-detail', kwargs={'pk': self.pk})

class RequestStatus(models.Model):
    status_types = [
            ("ACCEPTED", "Accepted"),
            ("DENIED", "Denied"),
            ("WAITING", "Waiting For Response") 
        ]
    status = models.CharField(max_length=8, choices=status_types, default="WAITING")
    

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    request_status = models.OneToOneField(RequestStatus, on_delete=models.CASCADE)
    pickup_location = AddressField(null=True)
    date_requested = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.username} requests {self.ride.creator.username}'












    
    

