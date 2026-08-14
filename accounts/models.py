from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True, default='')
    address = models.CharField(max_length=150, blank=True, default='')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    
