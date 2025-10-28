from rest_framework import serializers
from .models import Carrito, ItemCarrito

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')
    
    class Meta:
        model = ItemCarrito
        fields = ['producto', 'producto_nombre', 'cantidad']

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(source='itemcarrito_set', many=True, read_only=True)
    
    class Meta:
        model = Carrito
        fields = ['id', 'creado_en', 'items']