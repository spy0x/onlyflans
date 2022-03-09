from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("indice")

def about(request):
    return HttpResponse("acerca")

def welcome(request):
    response = "bienvenido cliente"
    return HttpResponse(response)

