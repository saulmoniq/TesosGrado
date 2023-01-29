from django.urls import path, include
from . import views
app_name="teg"
urlpatterns = [
    path('', views.home, name='home'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("perfil", views.perfil, name="perfil"),
    path("psicologo", views.postulate, name="psicologo"),
    path("publicarse", views.createPost.as_view(), name="publicarse"),
    path("404", views.error, name="404"),
    path("publicaciones", views.publicaciones.as_view(), name="publicaciones"),
    # path('<pk>/actualizarPost', views.actualizarPost.as_view(), name="actualizarPost"),
    path('<pk>/borrarpublicacion', views.borrarpublicacion.as_view(), name="borrarpublicacion"),
    path('buscador', views.buscador, name="buscador"),

]