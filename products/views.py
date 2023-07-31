from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductDetailSerializer
from .models import Product
# Create your views here.

class ProductViewset(ModelViewSet):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()