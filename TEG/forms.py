from django import forms
from django.forms import ModelForm
from .models import piscologoPublicacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class nuevoUsuario(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
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
		    'value': '',
		    'readonly' : True,
		    'class': 'usuariomod',
		    'hidden': True,
		}
	   ),
	}
