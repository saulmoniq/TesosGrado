from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .models import usuario, historiaContrasena, piscologoPublicacion
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import nuevoUsuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import createPost
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin 
from django.contrib import messages


# Create your views here.
from django.urls import path
from . import views

# Inicio
def home(request):
    return render(request, 'home.html')



# 404
def error(request):
    return render(request, '404.html')

# perfil
def perfil(request):
    return render(request, 'perfil.html')



# Enviar email-form
def send_email(mail, nombre, cedula, FVP, Teléfono, nombreusuario, Ubicacion):
	context = {
		'mail': mail,
		'nombre' : nombre,
		'cedula' : cedula,
		'FVP' : FVP,
		'Teléfono' : Teléfono,
		'nombreusuario' : nombreusuario,
		'Ubicacion' : Ubicacion
			}
	template = get_template('correo.html')
	content = template.render(context)

	email = EmailMultiAlternatives(
		'Un correo de prueba',
		'CodigoFacilito',
		settings.EMAIL_HOST_USER,
		[mail],
		cc=['monique26331419@usm.edu.ve']

	)
	email.attach_alternative(content, 'text/html')
	email.send()

# enviar email con informacion
def postulate(request):
	if request.method == "POST":
		mail=request.POST.get('mail')
		nombre=request.POST.get('nombre')
		cedula=request.POST.get('cedula')
		FVP=request.POST.get('FVP')
		Teléfono=request.POST.get('Teléfono')
		nombreusuario=request.POST.get('nombreusuario')
		Ubicacion=request.POST.get('Ubicacion')

		send_email(mail, nombre, cedula, FVP, Teléfono, nombreusuario, Ubicacion )
    
	return render(request, 'postulate_psico.html', {})

# Registro
def register_request(request):
	if request.method == "POST":
		form = nuevoUsuario(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("teg:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = nuevoUsuario()
	return render (request=request, template_name="register.html", context={"register_form":form})

# login
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("teg:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

# logout
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("teg:home")

#Crear post piscologo


# publicar con autenticacion, activar.
# class createPost(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#   login_url="/login"
#   model = piscologoPublicacion
#   form_class = createPost
#   template_name = "publicarse.html"
  
#   def test_func(self):
#     return self.request.user.groups.filter(name='psicologo').exists()

#   def handle_no_permission(self):
#     messages.error(self.request, 'No tienes permisos para ver esta página, debes iniciar sesión y ser un psicólogo aprobado')
#     return redirect('/404')


#   publicarse para pruebas, borrar al concluir
class createPost(CreateView):
  login_url="/login"
  model = piscologoPublicacion
  form_class = createPost
  template_name = "publicarse.html"
  success_url = "/publicaciones"

# # Actualizar publicaciones
# class actualizarPost(UpdateView):
#   template_name = "update_publicaciones.html"
#   model = piscologoPublicacion
#   form_class = createPost

#   mostrar publicaciones
class publicaciones(ListView):
  model = piscologoPublicacion
  template_name = "list_publicaciones.html"


class borrarpublicacion(DeleteView):
  model = piscologoPublicacion
  success_url = '/publicaciones'
  template_name = "borrar_publicacion.html"