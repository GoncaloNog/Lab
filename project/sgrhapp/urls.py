from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from sgrhapp import views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Página inicial que renderiza o template
    path('home/', views.home_view, name='home'),
    path('registar-ponto/', views.registar_ponto_view, name='registar_ponto'),
    path('colaboradores/', views.lista_colaboradores_view, name='lista_colaboradores'),
    path('colaboradores/novo/', views.adicionar_colaborador_view, name='adicionar_colaborador'),
    path('relatorios/', views.relatorios_view, name='relatorios'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]