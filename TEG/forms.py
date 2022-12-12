from django import forms
from .models import usuario

class registroUsuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = "__all__"