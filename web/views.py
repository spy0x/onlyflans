from django.shortcuts import render
from .models import ContactFormModelForm

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ContactFormForm
from .models import Flan, ContactForm
from django.contrib.auth.decorators import login_required


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'contenido' : 'Índice',
        'lista_flanes_publicos' : flanes_publicos}
    return render(request, 'index.html', context)

def about(request):
    context = {'contenido' : 'Acerca'}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    context = {
        'contenido' : 'Contacto',
        'form' : form}
    return render(request, 'contact.html', context)

def success(request):
    context = {'contenido' : 'Gracias por contactarte con OnlyFlans, te responderemos en breve'}
    return render(request, 'success.html', context)

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'contenido' : 'Bienvenido Cliente',
        'lista_flanes_privados' : flanes_privados}
    return render(request, 'welcome.html', context)

