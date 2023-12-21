from django.contrib.auth.models import User
from django.db import models


# NEED TO MIGRATE WHEN READY
class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="clubs")
    created_by = models.ForeignKey(User, related_name="created_clubs", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_add_now = True)


