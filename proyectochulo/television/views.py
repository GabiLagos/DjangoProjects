from django.shortcuts import render
from television.models import ServiceSeries, ServicePersonaje  

def index (request):
    return render (request, 'pages/index.html' )

def metodoSeries(request):
    servicio=ServiceSeries()
    series=servicio.getSeries()
    context = {
        "series" : series
        
    }
    return render (request, 'pages/series.html', context)

def metodoPersonajes(request):
    if ('id' in request.GET):
        servperson=ServicePersonaje 
        idseries=id
        person=servperson.getPersonajesSeries(idseries)
        context = {
            "person" : person
            }
        return render (request, 'pages/personajes.html', context)
    else:
        return render (request, 'pages/personajes.html')
    




