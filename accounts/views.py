from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def employee_list(request):
    context = {'employee_list': User.objects.all()}
    return render(request, "employee_list.html", context)