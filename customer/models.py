from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    userref = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userrev')
    address = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender =models.CharField(max_length=6)
    def __str__(self):
        return self.userref.username
