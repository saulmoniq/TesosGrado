from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import usuario
from .forms import registroUsuario

# Create your views here.
from django.urls import path
from . import views

def home(request):
    return render(request, 'home.html')

class registroUsuario(CreateView):
    template_name = "registro_usuario.html"
    form_class = registroUsuario
    model = usuario
