from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
from drf_spectacular.utils import  extend_schema
# Create your views here.

@extend_schema(tags=['Productos'])
class ProductoViewSet(viewsets.ModelViewSet):
    """CRUD y listado para Productos con HATEOAS en el Serializer."""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)