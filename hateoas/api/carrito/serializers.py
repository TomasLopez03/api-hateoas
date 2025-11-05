from rest_framework import serializers
from .models import Carrito, ItemCarrito

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')
    
    class Meta:
        model = ItemCarrito
        fields = ['producto', 'producto_nombre', 'cantidad']

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(source='itemcarrito_set', many=True, read_only=True)
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Carrito
        fields = ['id', 'creado_en', 'items', '_links']

    def get__links(self, obj):
        """Genera enlaces HATEOAS para el carrito."""
        request = self.context.get('request')
        if not request:
            return {}

        return {
            'self': {
                'href': request.build_absolute_uri(f'/api/carritos/{obj.id}/'),
                'method': 'GET',
            },
            'create_order': {
                'href': request.build_absolute_uri('/api/ordenes/'),
                'method': 'POST',
                'description': 'Crea una orden a partir de este carrito.',
                'fields': {
                    'carrito': {
                        'type': 'integer',
                        'required': True,
                        'description': 'ID del carrito para crear la orden. Usa el id: ' + str(obj.id)
                    },
                    'estatus': {
                        'type': 'string',
                        'required': False,
                        'description': "Estatus inicial de la orden (por defecto 'pendiente')."
                    },
                }
            },
        } 