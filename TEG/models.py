from unittest.util import _MAX_LENGTH
from django.db import models
import datetime


# Create your models here.

#Tablas con contenido fijo - De soporte




#Tablas variables
class usuario (models.Model):
    nombre = models.CharField(max_length=20)
    fechaNacimiento = models.DateTimeField(blank=True, default=datetime.date.today)
    cedula = models.IntegerField(max_length=8, default= 0)
    telefono = models.IntegerField(max_length=8, default= 0)
    correo = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=10)
    #FK's
    

    