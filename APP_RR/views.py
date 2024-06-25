# APP_RR/views.py
from django.shortcuts import render, redirect
from .models import Articulo
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    return render(request, 'apprr/index.html', context)

def qsomos(request):
    context = {}
    return render(request, 'apprr/Qsomos.html', context)

def galeria(request):
    context = {}
    return render(request, 'apprr/galeria.html', context)

def contactanos(request):
    context = {}
    return render(request, 'apprr/contactanos.html', context)

def registro(request):
    context = {}
    return render(request, 'apprr/registro.html', context)

def listado_articulos(request):
    articulos = Articulo.objects.all()

    perfil = request.session.get('perfil')

    context = {
        'articulos': articulos
    }
    return render(request, 'apprr/listado_articulos.html', context)



