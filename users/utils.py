from django.contrib.auth.hashers import make_password
from .models import UserProfile

def create_user_profile(username, email, password, **extra_fields):
    if not email:
        raise ValueError("The Email field must be set")
    
    user = UserProfile(username=username, email=email, **extra_fields)
    user.password = make_password(password)  # Hash the password before saving
    user.save()
    return user
