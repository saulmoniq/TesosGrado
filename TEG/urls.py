from django.urls import path
from . import views
app_name="teg"
urlpatterns = [
    path('', views.home, name='home'),
    path("register", views.register_request, name="register")
]