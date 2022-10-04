from django.shortcuts import render

# Create your views here.
from django.urls import path
from . import views

def home(request):
    return render(request, 'home.html')