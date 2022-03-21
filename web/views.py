from django.shortcuts import render
from .models import Flan

from django.http import HttpResponse
from django.template import loader


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'contenido' : 'indice',
        'lista_flanes_publicos' : flanes_publicos}
    return render(request, 'index.html', context)

def about(request):
    context = {'contenido' : 'acerca'}
    return render(request, 'about.html', context)

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'contenido' : 'bienvenido cliente',
        'lista_flanes_privados' : flanes_privados}
    return render(request, 'welcome.html', context)

