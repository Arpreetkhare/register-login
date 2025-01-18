from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserProfile(models.Model):
    USER_TYPES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.username

    