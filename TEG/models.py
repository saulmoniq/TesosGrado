from contextlib import nullcontext
from ctypes import FormatError
from email.policy import default
from random import choices
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django import forms

#Tablas con contenido fijo - De soporte
# Metodo de pago para publicaciones.
class plataformasAceptadas(models.Model):
  PagoMovil = "PM"
  Zelle = "ZE"
  Airtm = "AT"

  PAYMENT_CHOICES = [
    (PagoMovil, "PagoMovil"),
    (Zelle, "Zelle"),
    (Airtm, "Airtm"),
  ]

  nombre = models.CharField(max_length=2,choices=PAYMENT_CHOICES,default=PagoMovil)
  descripcion = models.CharField(max_length=50,default="")

  def __str__(self):
    return self.nombre

#Tablas variables



# Preguntas de seguridad para cada usuario
class preguntasSeguridad(models.Model):
    pregunta = models.CharField(max_length = 50)
    respuesta = models.CharField(max_length = 50)
    def __str__(self):
        return self.pregunta



# usuario main desactivaod previo al conocer el abstracbase
class usuarioInfo (models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   cedula = models.IntegerField("Cédula", default= 0)
   telefono = models.IntegerField("Teléfono",default= 0)
   ubicacion = models.CharField("Ubicación", max_length=10)
        #FK's
   def __str__(self):
        return str(self.user.username)
   def get_absolute_url(self):
        return "/" 

# publicaciones de psicologos 
class piscologoPublicacion (models.Model):
    usuario = models.ForeignKey(usuarioInfo, null=True, on_delete=models.CASCADE)
    IDplataformas = models.ForeignKey(plataformasAceptadas, null=True, on_delete=models.CASCADE)
    precio = models.IntegerField("Precio", default=15)
    duracionTerapia = models.IntegerField("Duración de terapia", default=1)  

    def __str__(self):
        return str(self.usuario.user.email)
    def get_absolute_url(self):
        return "/publicaciones"

