from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User


def employee_list(request):
    context = {"employee_list": User.objects.all()}
    return render(request, "employee_list.html", context)
