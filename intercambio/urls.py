from django.urls import path, include
from rest_framework import routers
from django.urls import path
from .views import *

urlpatterns = [
    path('carreras/', listaCarreras.as_view(), name='lista_carreras'),
    path('carreras/<int:id>/', listaCarreras.as_view(), name='carrera_detalle'),
    path('mov-carreras/', movDestinos.as_view(), name='movDestinos'),
]