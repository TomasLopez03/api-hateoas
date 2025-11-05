from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Producto que incluye enlaces HATEOAS.
    """
    _links = serializers.SerializerMethodField()
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', '_links']
        
    def get__links(self, obj):
        """Genera los enlaces HATEOAS para cada producto."""
        request = self.context.get('request')
        if not request:
            return {}
            
        return {
            'self': {
                'href': request.build_absolute_uri(f'/api/productos/{obj.id}/'),
                'method': 'GET',
            },
            'list_all': {
                'href': request.build_absolute_uri('/api/productos/'),
                'method': 'GET',
            },
            'add_to_cart': {
                # Asumimos un endpoint para agregar a un carrito, p.ej. /carritos/add/
                'href': request.build_absolute_uri(f'/api/carritos/add/{obj.id}/'), 
                'method': 'POST',
                'description': 'POST {"cantidad": 1} para añadir este producto al carrito activo/nuevo.',
            },
        }