from django import forms
from .models import usuario

class registroUsuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ("nombre", "fechaNacimiento", "cedula", "telefono", "correo", "username", "ubicacion", "passActual", "tipoDeUsuario")
