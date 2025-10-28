from django.db import models
from api.carrito.models import Carrito

# Create your models here.
class Orden(models.Model):
    """Modelo para representar una orden de compra."""
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente de Pago'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
    ]
    carrito = models.OneToOneField(Carrito, on_delete=models.PROTECT) # PROTECT para no borrar el carrito si la orden existe
    estatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    fecha_orden = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id} - {self.get_estatus_display()}"