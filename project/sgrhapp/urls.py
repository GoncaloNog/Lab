from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from sgrhapp import views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Página inicial que renderiza o template
    path('home/', views.home_view, name='home'),
]