from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import usuario
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import nuevoUsuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout



# Create your views here.
from django.urls import path
from . import views

def home(request):
    return render(request, 'home.html')

def perfil(request):
    return render(request, 'perfil.html')

def postulate(request):
    return render(request, 'postulate_psico.html')

def register_request(request):
	if request.method == "POST":
		form = nuevoUsuario(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("teg:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = nuevoUsuario()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("teg:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("teg:home")