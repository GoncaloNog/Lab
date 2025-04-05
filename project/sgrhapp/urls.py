from django.urls import path
from django.contrib import admin
from sgrhapp import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login')  # Página inicial que renderiza o template
]