from django.urls import path
from aplicacion import views

urlpatterns = [
   
    path('', views.index, name='index'),
    
    path('friday/', views.metodo_viernes,name='viernes'),
    
    path('listas/', views.listas,name='listas'),
    
    path('peli/', views.paginaPelicula, name='peli'),
    
    ]
