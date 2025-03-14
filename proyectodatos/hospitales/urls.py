from django.urls import path
from hospitales import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('deptbbdd/', views.deptBBDD, name='deptBBDD' ),
    
    path('hospbbdd/', views.hospBBDD, name='hospBBDD' ),
    
    path('insertdeptpbbdd/', views.insertDeptBBDD, name='insertDeptBBDD' ),
    
    path('borrardeptpbbdd/', views.borrarDeptBBDD, name='borrarDeptBBDD' ),
    
    path('detallesdeptpbbdd', views.detallesDeptBBDD, name = 'detallesDeptBBDD'),
    
    path('updatedeptbbdd/', views.updateDeptBBDD, name ='updateDeptBBDD' ),
    
    path( 'empdept/', views.EmpDept, name = 'EmpDept'),
    
]