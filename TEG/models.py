from contextlib import nullcontext
from ctypes import FormatError
from email.policy import default
from random import choices
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime



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



#Tablas variables



# Preguntas de seguridad para cada usuario
class preguntasSeguridad(models.Model):
    pregunta = models.CharField(max_length = 50)
    respuesta = models.CharField(max_length = 50)

#  Historial de contraseña necesario
class historiaContrasena (models.Model):
    passActual = models.CharField(max_length=20)
    passAntiguo = models.CharField(max_length=20)
    preguntas = models.ForeignKey(preguntasSeguridad,null=True, on_delete=models.CASCADE)


# usuario main
class usuario (models.Model):
    nombre = models.CharField(max_length=20)
    fechaNacimiento = models.DateTimeField(blank=True, default=datetime.date.today)
    cedula = models.IntegerField(max_length=8, default= 0)
    telefono = models.IntegerField(max_length=8, default= 0)
    correo = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=10)
    #FK's
    passUser = models.ForeignKey(historiaContrasena, null=True, on_delete=models.CASCADE)
    
# tipo de usuario - Para comprobar funcionamiento
class TipoDeUsuario(models.Model):
    psicologo = "PSI"
    paciente = "PAC"

    USER_TYPE = [
    (psicologo, "Psicólogo"),
    (paciente, "Paciente"),
  ]
    nombre = models.CharField(max_length=3, choices=USER_TYPE, default=paciente)



# registro de citas 


# publicaciones de psicologos 
class piscologoPublicacion (models.Model):
    IDusuario = models.ForeignKey(usuario, null=True, on_delete=models.CASCADE)
    IDplataformas = models.ForeignKey(plataformasAceptadas, null=True, default=models.CASCADE)
    precio = models.IntegerField(max_length=10, default=15)
    duracionTerapia = models.IntegerField(max_length=10, default=1)    

