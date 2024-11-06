from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import *
from .serializers import *
from django.shortcuts import render

class EscuelasMovViewSet(viewsets.ModelViewSet):
    queryset = EscuelasMov.objects.all()
    serializer_class = EscuelasMovSerializer

class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarreraSerializer

class CarrerasInterViewSet(viewsets.ModelViewSet):
    queryset = CarrerasInter.objects.all()
    serializer_class = CarrerasInterSerializer

class listaCarreras(generics.ListAPIView):
    serializer_class = CarreraSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = self.kwargs.get('id', None) 

        if id is not None:
            return Carreras.objects.filter(id=id)
            
        return Carreras.objects.all()

class movDestinos(generics.ListAPIView):
    serializer_class = CarrerasInterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = CarrerasInter.objects.all()
        carrera_id = self.request.query_params.get('carrera_id', None)
        disponible = self.request.query_params.get('disponible', None)

        if carrera_id is not None:
            queryset = queryset.filter(carreras_id=carrera_id)
        
        if disponible is not None:
            disponible = disponible.lower() == 'true'
            queryset = queryset.filter(disponible=disponible)

        return queryset