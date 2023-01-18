from django import forms
from .models import usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user