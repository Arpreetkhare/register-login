from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserSignupSerializer, UserProfileSerializer 

class SignupView(APIView):

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username , 'user_type': user.user_type})
        return Response(serializer.errors, status=400)


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
            
        user = UserProfile.objects.filter(username=username).first()
        if user is None  :
            return Response({'error': 'Invalid credentials'}, status=400)

        

        serializer = UserProfileSerializer(user)
        return Response({"user" : serializer.data})
        

class DashboardView(APIView):

    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users,many = True)
        return Response(serializer.data)
