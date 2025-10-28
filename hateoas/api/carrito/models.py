from django.db import models
from api.productos.models import Producto

# Create your models here.
class Carrito(models.Model):
    """Modelo para representar el carrito de compras del usuario."""
    # Podría incluir un campo 'usuario' si fuera una API con autenticación
    creado_en = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    
    def __str__(self):
        return f"Carrito #{self.id}"
    
class ItemCarrito(models.Model):
    """Modelo intermedio para manejar productos y cantidad en el carrito."""
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('carrito', 'producto')
        
    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en Carrito #{self.carrito.id}"