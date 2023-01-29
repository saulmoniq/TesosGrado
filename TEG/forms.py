from django import forms
from django.forms import ModelForm
from .models import usuario, piscologoPublicacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class nuevoUsuario(UserCreationForm):
	# psicologo = "PSI"
	# paciente = "pag"

	# psioPaciente= [
	# 	(psicologo, "Psicólogo"),
	# 	(paciente, "Paciente"),
	# ]

	email = forms.EmailField(required=True)
	# nombre = forms.CharField(label='First name', max_length=100)
	# apellido = forms.CharField()
	# fechaNacimiento = forms.DateTimeField()
	# cedula = forms.IntegerField()
	# telefono = forms.IntegerField()
	# ubicacion = forms.CharField()
	# tipo = forms.ChoiceField(choices=psioPaciente, required=True)

	class Meta:
		model = User
		# fields = ("nombre","apellido","tipo","fechaNacimiento","cedula", "telefono", "ubicacion", "username", "email", "password1", "password2")
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(nuevoUsuario, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# crate post psicologo
class createPost(forms.ModelForm):
    class Meta:
        model = piscologoPublicacion
        fields = "__all__"
        widgets = {
	   'usuario' : forms.TextInput(
		attrs={
		    'value': piscologoPublicacion.usuario,
		    'readonly' : True,
		}
	   ),
	}
