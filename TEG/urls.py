from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro', views.registroUsuario.as_view(), name="registroUsuario"),

]