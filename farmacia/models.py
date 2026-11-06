# farmacia/models.py
from django.db import models

class Medicamento(models.Model):
    nombre_producto = models.CharField(
        max_length=150,
        verbose_name="Nombre del Producto"
    )
    laboratorio = models.CharField(
        max_length=100,
        verbose_name="Laboratorio"
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio ($)"
    )
    requiere_receta = models.BooleanField(
        default=False,
        verbose_name="¿Requiere Receta Médica?"
    )

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ['nombre_producto']

    def __str__(self):
        return f"{self.nombre_producto} - {self.laboratorio}"