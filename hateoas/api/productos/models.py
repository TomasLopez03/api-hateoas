from django.db import models

# Create your models here.
class Producto(models.Model):
    """Modelo para representar un producto en el inventario."""
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre