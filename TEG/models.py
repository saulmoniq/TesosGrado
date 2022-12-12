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

  def __str__(self):
    return self.nombre

#Tablas variables



# Preguntas de seguridad para cada usuario
class preguntasSeguridad(models.Model):
    pregunta = models.CharField(max_length = 50)
    respuesta = models.CharField(max_length = 50)
    def __str__(self):
        return self.pregunta



#  Historial de contraseña necesario
class historiaContrasena (models.Model):
    passActual = models.CharField(max_length=20)
    passAntiguo = models.CharField(max_length=20)
    preguntas = models.ForeignKey(preguntasSeguridad,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.passActual

# tipo de usuario - Para comprobar funcionamiento
class TipoDeUsuario(models.Model):
    psicologo = "PSI"
    paciente = "PAC"

    USER_TYPE = [
    (psicologo, "Psicólogo"),
    (paciente, "Paciente"),
  ]
    tipo = models.CharField(max_length=3, choices=USER_TYPE, default=paciente)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo

# registro de citas 
class citas(models.Model):
    tipoUsuario = models.ForeignKey(TipoDeUsuario, null=True, on_delete=models.CASCADE)
    fechaCita = models.DateTimeField()
    def __str__(self):
        return str(self.fechaCita)


# usuario main
class usuario (models.Model):
    nombre = models.CharField(max_length=20)
    fechaNacimiento = models.DateTimeField()
    cedula = models.IntegerField(default= 0)
    telefono = models.IntegerField(default= 0)
    correo = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=10)
    #FK's
    passUser = models.ForeignKey(historiaContrasena, null=True, on_delete=models.CASCADE)
    citas = models.ForeignKey(citas, null=True, on_delete=models.CASCADE)
    tipoDeUsuario = models.ForeignKey(TipoDeUsuario, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

# publicaciones de psicologos 
class piscologoPublicacion (models.Model):
    IDusuario = models.ForeignKey(usuario, null=True, on_delete=models.CASCADE)
    IDplataformas = models.ForeignKey(plataformasAceptadas, null=True, on_delete=models.CASCADE)
    precio = models.IntegerField(default=15)
    duracionTerapia = models.IntegerField(default=1)  
    def __str__(self):
        return self.IDusuario + " " + self.precio 

# Parametros pass
# class parametrosPass (models.Model):
#     longitudMin = models.IntegerField(max_length=8)
#     longitudMax = models.IntegerField(max_length=20)
#     intentosBloqueo = models.IntegerField(max_length=3)
    
     