from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {'titulo': 'HOME', 'contenido' : 'indice'}
    return render(request, 'base.html', context)

def about(request):
    context = {'titulo': 'ABOUT', 'contenido' : 'acerca'}
    return render(request, 'base.html', context)

def welcome(request):
    context = {'titulo': 'WELCOME', 'contenido' : 'bienvenido cliente'}
    return render(request, 'base.html', context)

