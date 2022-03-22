from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ContactFormForm
from .models import Flan, ContactForm


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'contenido' : 'Índice',
        'lista_flanes_publicos' : flanes_publicos}
    return render(request, 'index.html', context)

def about(request):
    context = {'contenido' : 'acerca'}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()
    context = {
        'contenido' : 'contacto',
        'form' : form}
    return render(request, 'contact.html', context)

def success(request):
    context = {'contenido' : 'Gracias por contactarte con OnlyFlans, te responderemos en breve'}
    return render(request, 'success.html', context)

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'contenido' : 'Bienvenido cliente',
        'lista_flanes_privados' : flanes_privados}
    return render(request, 'welcome.html', context)

