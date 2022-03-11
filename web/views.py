from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {'contenido' : 'indice'}
    return render(request, 'index.html', context)

def about(request):
    context = {'contenido' : 'acerca'}
    return render(request, 'about.html', context)

def welcome(request):
    context = {'contenido' : 'bienvenido cliente'}
    return render(request, 'welcome.html', context)

