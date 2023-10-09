from django.contrib import admin
from .models import Ride, Request, RequestStatus, Car, User_Car

admin.site.register(Car)
admin.site.register(User_Car)
admin.site.register(Ride)
admin.site.register(Request)
admin.site.register(RequestStatus)

