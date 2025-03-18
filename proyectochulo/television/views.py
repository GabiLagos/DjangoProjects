from django.shortcuts import render
from television.models import ServiceSeries  

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
    servperson=ServiceSeries() 
    if ('id' in request.GET):
        id=request.GET['id']
        person=servperson.getPersonajesSeries(id)
        context = {
            "person" : person
            }
        return render (request, 'pages/personajes.html', context)
    else: 
        person=servperson.getPersonajes()
        context = {
            "person" : person
            }
        return render (request, 'pages/personajes.html', context)

def modificarPersonaje(request):
    servicio=ServiceSeries()
    if ('cajaimagen' in request.POST):
        idperson=request.POST['cajaperson']
        nombre= request.POST['cajanombre']
        imagen= request.POST['cajaimagen']
        idserie= request.POST['cajaserie']
        servicio.updatePersonaje(idperson, nombre, imagen, idserie)
        return render (request, 'pages/modificarpersonajes.html')
    elif ('idperson' in request.GET):
        idperson=request.GET['idperson']
        personaje = servicio.findPersonajes(idperson)
        serie= servicio.getSeries()
        context= {
            "person":personaje,
            "serie":serie
            }
        return render (request, 'pages/modificarpersonajes.html', context)
    else: 
        return render (request, 'pages/modificarpersonajes.html')
    
    
def updatePersonajeSerie(request):
    servicio=ServiceSeries()
    personajes=servicio.getPersonajes()
    series=servicio.getSeries()
    return render (request, 'pages/updatepersonajeserie.html')
    
        
    
    

    
    



