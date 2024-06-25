from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='principal'),
    path('qsomos/', views.qsomos, name='qsomos'),
    path('galeria/', views.galeria, name='galeria'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('registro/', views.registro, name='registro'),
    path('listado_articulos/', views.listado_articulos, name='listado_articulos'),
]

