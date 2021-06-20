from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ProductoSerializer
from .models import producto


class ProductoViewSet(viewsets.ModelViewSet):
    
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer
