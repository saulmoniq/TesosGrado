from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


# class registroUsuario(forms.ModelForm):
#     class Meta:
#         model = usuario
#         fields = ("nombre", "fechaNacimiento", "cedula", "telefono", "correo", "username", "ubicacion", "passActual", "tipoDeUsuario")

# class form_registroUsuario(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(form_registroUsuario, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


# Create your forms here.


class NewUserForm(UserCreationForm):
	psicologo = "PSI"
	paciente = "pag"

	psioPaciente= [
		(psicologo, "Psicólogo"),
		(paciente, "Paciente"),
	]
	email = forms.EmailField(required=True)
	nombre = forms.CharField()
	apellido = forms.CharField()
	fechaNacimiento = forms.DateTimeField()
	cedula = forms.IntegerField()
	telefono = forms.IntegerField()
	ubicacion = forms.CharField()
	paciente = forms.ChoiceField(choices=psioPaciente, required=True)

	class Meta:
		model = User
		fields = ("nombre","apellido","paciente","fechaNacimiento","cedula", "telefono", "ubicacion", "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email'],
		if commit:
			user.save()
		return user