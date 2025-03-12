from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'informacion/index.html')

def pelis(request):
    
    return render(request, 'informacion/pelis.html')

def tabla(request):
    #tenemos que preguntar la caja tiene datos
    if('mult' in request.POST):
        #desarrollo de la conjetura de la tabla de multiplicar
        multi = int (request.POST['mult']) 
        xx=multi
        c=0
        x=0
        listatabla = []
        
        while (c!=10):
            c=c+1
            x=multi*c
            listatabla.append({"numi":xx, "op": c, "result": x})
        
        context = {
            "tablaMult":listatabla
        }
        
        return render(request, 'informacion/tabla.html', context)
    
    else:#si no hay informacion, seguimos como antes
        return render(request, 'informacion/tabla.html')


def collatz(request):
     #tenemos que preguntar alguna de las cajas tiene datios
    if('cajanum' in request.POST):
        #desarrollo de la conjetura de Collatz
        numero = int (request.POST['cajanum']) 
        
        listanum = []
        
        while (numero != 1):
            if (numero % 2 == 0):
                numero=int(numero/2)
            else:
                numero= int(1+numero*3)
                
            listanum.append(numero)
        
        context = {
            "numerosCollatz":listanum
        }
        
        return render(request, 'informacion/collatz.html', context)
    
    #si no hay informacion, seguimos como antes
    else:
        return render(request, 'informacion/collatz.html')


def sumarnumeros(request):
    #tenemos que preguntar alguna de las cajas tiene datios
    if('cajanum1' in request.POST):
        num1 = request.POST['cajanum1']
        num2 = request.POST['cajanum2']
        suma = int(num1) + int(num2)
    #devuelvo el resultado de la suma
        context = {
        "resultado" : suma,
        "numero1" : num1,
        "numero2": num2,
        }
        return render(request, 'informacion/sumarnumeros.html', context)
    #si no hay informacion, seguimos como antes
    else:
        return render(request, 'informacion/sumarnumeros.html')

def saludo(request):
    #tenemos que preguntar si hemos recibido datos del formulario
    if('cajanombre' in request.POST):
        nombreRecibido = request.POST['cajanombre']
    #si se han ingresado datos, devolvemos el nombre del formulario
        context = {
        "nombre" : nombreRecibido
        }
        return render(request, 'informacion/saludo.html', context)
    #si no hay informacion, seguimos como antes
    else:
        return render(request, 'informacion/saludo.html')


def colores(request):
    #recuperamos la variable micolor que envia GET. Pero debemos comprobar si efectivamente hemos recibido dicha variable
    if('micolor'in request.GET):
        colorRecibido = request.GET['micolor']
    #ahora devolvemos el color recibido
        context = {
        "colordibujo" : colorRecibido
        }
        return render(request, 'informacion/colores.html', context)
    else:
        return render(request, 'informacion/colores.html')

def futbol(request):
    nombre = "Real Madrid"
    data = {
        "equipo" : nombre 
        }
    return render(request, 'informacion/futbol.html', data)



def jugadores(request):
    jugadores = [
        {"demarcacion": "Portero", "numero": 1, "nombre": "Thibaut Courtois"},
        {"demarcacion": "Portero", "numero": 13, "nombre": "Andriy Lunin"},
        {"demarcacion": "Defensa", "numero": 35, "nombre": "Raul Ascencio"},
        {"demarcacion": "Defensa", "numero": 4, "nombre": "David Alaba"},
        {"demarcacion": "Defensa", "numero": 22, "nombre": "Antonio Rüdiger"},
        {"demarcacion": "Defensa", "numero": 23, "nombre": "Ferland Mendy"},
        {"demarcacion": "Centrocampista", "numero": 25, "nombre": "Eduardo Camavinga"},
        {"demarcacion": "Centrocampista", "numero": 5, "nombre": "Jude Bellingham"},
        {"demarcacion": "Centrocampista", "numero": 8, "nombre": "Federico Valverde"},
        {"demarcacion": "Centrocampista", "numero": 10, "nombre": "Luka Modric"},
        {"demarcacion": "Delantero", "numero": 11, "nombre": "Rodrygo Goes"},
        {"demarcacion": "Delantero", "numero": 20, "nombre": "Vinícius Júnior"},
        {"demarcacion": "Delantero", "numero": 7, "nombre": "Kylian Mbappé"},
        {"demarcacion": "Delantero", "numero": 30, "nombre": "Endrick"},
        {"demarcacion": "Centrocampista", "numero": 28, "nombre": "Fran González"},
        {"demarcacion": "Centrocampista", "numero": 27, "nombre": "Arda Güler"},
    ]
    context = {
        "jug": jugadores
    }
    return render(request, 'informacion/jugadores.html', context)
