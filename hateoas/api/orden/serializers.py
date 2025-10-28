from rest_framework import serializers
from .models import Orden

class OrdenSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Orden con lógica HATEOAS condicional basada en 'estatus'.
    """
    _links = serializers.SerializerMethodField()
    carrito_id = serializers.ReadOnlyField(source='carrito.id')

    class Meta:
        model = Orden
        fields = ['id', 'carrito_id', 'estatus', 'fecha_orden', '_links']

    def get__links(self, obj):
        """Genera enlaces condicionales según el estatus de la orden."""
        request = self.context.get('request')
        if not request:
            return {}

        links = {
            'self': {
                'href': request.build_absolute_uri(f'/ordenes/{obj.id}/'),
                'method': 'GET',
            },
            'list_all': {
                'href': request.build_absolute_uri('/ordenes/'),
                'method': 'GET',
            },
        }
        
        # --- Lógica Condicional HATEOAS ---
        if obj.estatus == 'pendiente':
            links['pay'] = {
                'href': request.build_absolute_uri(f'/ordenes/{obj.id}/pay/'),
                'method': 'POST',
                'description': 'Confirma el pago de la orden.'
            }
            links['cancel'] = {
                'href': request.build_absolute_uri(f'/ordenes/{obj.id}/cancel/'),
                'method': 'DELETE',
                'description': 'Cancela la orden.'
            }
        elif obj.estatus == 'pagado':
            links['track_shipment'] = {
                'href': request.build_absolute_uri(f'/ordenes/{obj.id}/rastrear/'),
                'method': 'GET',
                'description': 'Rastrea el envío del pedido.'
            }
            links['refund'] = {
                'href': request.build_absolute_uri(f'/ordenes/{obj.id}/reembolsar/'),
                'method': 'POST',
                'description': 'Solicita un reembolso de la orden.'
            }
        # Si 'cancelado', solo se muestran 'self' y 'list_all' (los que ya están en 'links')

        return links