from django.http import HttpResponse
from django.http import JsonResponse
import json
#Utilities
from datetime import datetime
#Django es python lo que nos dice que se puede escribir funciones donde se desee
#Las vistas SIEMPRE reciben un requests que es el objeto del requests


def hello_world(request):
    #Se tiene que retornar una instancia de la clase HttpResponse
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))
#Método para ordenar números
def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json')
"""Valida la edad de la persona que ingresa
   el orden en el que se coloquen los parámetros en el URLPatterns
   tiene que ser el mismo en el que se reciben"""
def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hi {}'.format(name)
    return HttpResponse(message)
