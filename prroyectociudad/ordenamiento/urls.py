"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parroquias/', views.listar_parroquias_y_barrios, 
         name='listar_parroquias'),
    path('barrios/', views.listar_barrios, 
         name='listar_barrios'),
    path('parroquias/crear/', views.crear_parroquia, 
         name='crear_parroquia'),
    path('barrios/crear/', views.crear_barrio, 
         name='crear_barrio'),
]
