from django.http import HttpResponse
#from django.template import Templat, Contex
from django.template.loader import get_template
from django.shortcuts import render
import datetime


class taco_especial(object):
    def __init__(self, pastor, queso):
        self.pastor = pastor
        self.queso = queso


def menu(request):
    el_mejor=taco_especial("pastor", "queso")
    
    tacos = ["suadero", "pastor", "campehana", "bistek", "chorizo"]
    gringas = ["suadero", "pastor", "campehana", "bistek", "chorizo"]
    tortas = ["suadero", "pastor", "campehana", "bistek", "chorizo"]
    bebidas = ["coca", "jarrito", "boing"]

    #fecha.hoy = datetime.datetime.now()

    return render(request, "superior/base.html", {"el_mejor":el_mejor, "tacos":tacos, "gringas":gringas, "tortas":tortas, "bebidas":bebidas})

def ubicacion(request):

    return render(request, "superior/ubicacion.html")

def registro(request):

    return render(request, "superior/registro.html")
