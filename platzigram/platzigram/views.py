""" Platzigram views
"""
#django
from django.http import HttpResponse, JsonResponse

#utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')



def sort_integers(request):
    """returns a json response with sorted integers """
    numeros = request.GET['numbers']
    numeros_string = numeros.split(',') 
    numeros_lista = [int(i) for i in numeros_string]
    numeros_lista = sorted(numeros_lista)
    
    #response = JsonResponse(numeros_lista, safe=False)
    #import pdb; pdb.set_trace()
    data = {
        'status': 'ok',
        'numbers' : numeros_lista,
        'message' : 'interger sorted successfully'
    }
    
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json' ) 
    #return JsonResponse(response, safe=False) #false no es un dic, True es un diccionario

def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, welcome to platzigram'
    
    return HttpResponse(message)
