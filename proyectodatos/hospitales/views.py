from django.shortcuts import render
from hospitales.models import ServiceDepartamentos, ServiceHospitales, ServiceEmpleados


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
    servicio = ServiceHospitales()
    hosp = servicio.getHospitales()
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
    
def updateDeptBBDD(request):
    if('boxnum' in request.POST):
        servicio = ServiceDepartamentos()
        num= request.POST['boxnum']
        nombre= request.POST['boxnombre']
        loc= request.POST['boxloc']
        registros = servicio.updateDepartamentos(nombre, loc, num)
        depts = servicio.getDepartamentos()
        context = {
            "departamentos": depts
        }
        return render(request, 'pages/departamentos.html', context)
    
    else:
        return render(request, 'pages/updatedept.html')
    
def borrarDeptBBDD(request):
    servicio = ServiceDepartamentos()
    if('cajanum' in request.POST):
        num= request.POST['cajanum']
        registros = servicio.deleteDepartamentos(num)
        depts = servicio.getDepartamentos()
        context = {
            "departamentos": depts
        }
        return render(request, 'pages/departamentos.html', context)
    
    elif('id' in request.GET):
        num = request.GET['id']
        context = {
            "numero": num
        }
        return render(request, 'pages/borrardept.html', context)
    
    elif('id' in request.GET):
        numer = request.GET['id']
        department = servicio.detallesDepartamento(numer)
        context = {
            "department" : department
        }
        return render(request, 'pages/updatedept.html', context)
    
    else:
        return render(request, 'pages/updatedept.html')
    
    
def detallesDeptBBDD(request):
    if ('id'in request.GET):
        servicio = ServiceDepartamentos()
        numero = request.GET['id']
        departamento = servicio.detallesDepartamento(numero)
        context = {
            "departamento" : departamento
        }
        return render(request, 'pages/detallesdept.html', context)
    else:
        return render(request, 'pages/detallesdept.html')
    
    
def EmpDept(request):
    if ('cajadept'in request.POST):
        num= request.POST['cajadept']
        servicio= ServiceEmpleados()
        emps= servicio.filtraEmpleados(num)
        context = {
            "empleados" : emps
        }
        return render(request, 'pages/empleadosdepartamento.html', context)
        
        
    else:
        servicio= ServiceEmpleados()
        emps = servicio.getEmpleados()
        context = {
            "empleados" : emps
        }
        return render(request, 'pages/empleadosdepartamento.html', context)
    
    
