from django.shortcuts import render
from hospitales.models import ServiceDepartamentos, ServiceHospitales


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def deptBBDD(request):
    servicio= ServiceDepartamentos()
    depts = servicio.getDepartamentos()
    context = {
        "departamentos" : depts
    }
    return render(request, 'pages/departamentos.html', context)

def hospBBDD(request):
    sevicio = ServiceHospitales()
    hosp = sevicio.getHospitales()
    context = {
        "hospitales" : hosp
    }
    return render (request, 'pages/hospitales.html', context)

def insertDeptBBDD(request):
    if('cajanum' in request.POST):
        servicio = ServiceDepartamentos()
        num= request.POST['cajanum']
        nombre= request.POST['cajanombre']
        loc= request.POST['cajaloc']
        registros = servicio.insertDepartamentos(num,nombre,loc)
        depts = servicio.getDepartamentos()
        context = {
            "departamentos": depts
        }
        return render(request, 'pages/departamentos.html', context)
    
    else:
        return render(request, 'pages/insertardept.html')
    
def borrarDeptBBDD(request):
    if('cajanum' in request.POST):
        servicio = ServiceDepartamentos()
        num= request.POST['cajanum']
        registros = servicio.deleteDepartamentos(num)
        depts = servicio.getDepartamentos()
        context = {
            "departamentos": depts
        }
        return render(request, 'pages/departamentos.html', context)
    
    else:
        return render(request, 'pages/borrardept.html')
    
    
