from rest_framework import serializers
from .models import UserProfile
from .utils import create_user_profile

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 
                  'password', 'confirm_password', 'address_line1', 'city', 'state', 
                  'pincode', 'user_type']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = create_user_profile(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email',
                  'address_line1', 'city', 'state', 'pincode', 'user_type']
