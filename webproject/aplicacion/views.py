from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def metodo_index(request):
    return HttpResponse("Mi primera página Django!!!")

def metodo_viernes(request):
    return render(request, 'aplicacion/viernes.html')
    #return HttpResponse ("HOY ES VIERNES!!!!")

def index(request):
    return render(request, 'aplicacion/index.html')

def listas(request):
     return render(request, 'aplicacion/listas.html')
