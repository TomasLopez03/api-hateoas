from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from api.productos.models import Producto
from .models import Carrito, ItemCarrito
from .serializers import CarritoSerializer, ItemCarritoSerializer

# Create your views here.
@extend_schema(tags=['Carritos'])
class CarritoViewSet(viewsets.GenericViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    
    @action(detail=False, methods=['post'], url_path='add/(?P<producto_id>[^/.]+)')
    def add_item(self, request, producto_id=None):
        """Endpoint para añadir un producto a un carrito (simulación simple)."""
        try:
            producto = Producto.objects.get(pk=producto_id)
        except Producto.DoesNotExist:
            return Response({'detail': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
            
        # Simplificación: Usar el primer carrito, o crear uno si no existe.
        carrito, created = Carrito.objects.get_or_create(id=1) 
        cantidad = request.data.get('cantidad', 1)
        
        item, created = ItemCarrito.objects.get_or_create(
            carrito=carrito, 
            producto=producto,
            defaults={'cantidad': cantidad}
        )
        if not created:
            item.cantidad += int(cantidad)
            item.save()

        serializer = self.get_serializer(carrito)
        return Response(serializer.data, status=status.HTTP_200_OK)