from django.shortcuts import render
import requests
from .models import Character


# Create your views here.
def index(request):
    return render(request, 'index.html', 
                        {'name':'Marcos',
                        'estado':'completado',
                        'next':'construir el scrapeador de Star Wars API'
                        })


def characters(request, page=None):
    if page is None:
        characters = Character.objects.all()
    else:
        # filtrar los personajes por pagina
        characters = Character.objects.filter(page=page)
    return render(request, 'character.html', {"characters": characters})

