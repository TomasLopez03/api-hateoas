from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import Orden
from .serializers import OrdenSerializer

# Create your views here.
@extend_schema(tags=['Ordenes'])
class OrdenViewSet(viewsets.ModelViewSet):
    """CRUD y acciones con estado para Órdenes."""
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        orden = self.get_object()
        if orden.estatus == 'pendiente':
            orden.estatus = 'pagado'
            orden.save()
            return Response({'status': 'Orden marcada como pagada'}, status=status.HTTP_200_OK)
        return Response({'status': f'La orden no se puede pagar, estado actual: {orden.estatus}'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def cancel(self, request, pk=None):
        orden = self.get_object()
        if orden.estatus == 'pendiente':
            orden.estatus = 'cancelado'
            orden.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'status': f'La orden no se puede cancelar, estado actual: {orden.estatus}'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def rastrear(self, request, pk=None):
        orden = self.get_object()
        if orden.estatus == 'pagado':
            # Lógica de rastreo simulada
            return Response({'status': 'En tránsito. Entrega estimada en 3 días.'}, status=status.HTTP_200_OK)
        return Response({'status': f'No se puede rastrear, estado actual: {orden.estatus}'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def reembolsar(self, request, pk=None):
        orden = self.get_object()
        if orden.estatus == 'pagado':
            # Lógica de reembolso simulada
            # Nota: Esto podría cambiar el estado de la orden a 'reembolsada' en una app real.
            return Response({'status': 'Reembolso procesado exitosamente.'}, status=status.HTTP_200_OK)
        return Response({'status': f'No se puede reembolsar, estado actual: {orden.estatus}'}, status=status.HTTP_400_BAD_REQUEST)