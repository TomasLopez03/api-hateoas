from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from drf_spectacular.utils import  extend_schema
# Create your views here.

@extend_schema(tags=['Productos'])
class ProductoViewSet(viewsets.ModelViewSet):
    """CRUD y listado para Productos con HATEOAS en el Serializer."""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer