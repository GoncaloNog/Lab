from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'sgrhapp/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login bem-sucedido, redirecionando para /home/")
            return redirect('home')  # Usa o nome da URL da home
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'sgrhapp/login.html')

@login_required
def home_view(request):
    if request.method == 'POST':
        print('ola')
        logout(request)
        return render(request, 'sgrhapp/login.html')
    return render(request, 'sgrhapp/home.html')

@login_required
def registar_ponto_view(request):
    return render(request, 'sgrhapp/registar_ponto.html')

@login_required
def lista_colaboradores_view(request):
    return render(request, 'sgrhapp/lista_colaboradores.html')

@login_required
def adicionar_colaborador_view(request):
    return render(request, 'sgrhapp/adicionar_colaborador.html')

@login_required
def relatorios_view(request):
    return render(request, 'sgrhapp/relatorios.html')