from django.urls import path
from .views import UserLogin, RegisterUserAPIView, employee_list

urlpatterns = [
    path("api/login", UserLogin.as_view()),
    path("api/register", RegisterUserAPIView.as_view()),
    
]
