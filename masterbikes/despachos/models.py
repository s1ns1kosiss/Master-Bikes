from django.db import models
from arriendos.models import Arriendo
from usuarios.models import Usuario

class Despacho(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_CAMINO', 'En camino'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    arriendo = models.ForeignKey(Arriendo, on_delete=models.CASCADE, related_name='despachos')
    direccion_entrega = models.CharField(max_length=255)
    fecha_despacho = models.DateTimeField()
    fecha_entregado = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='PENDIENTE')
    observaciones = models.TextField(blank=True, null=True)
    encargado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachos_asignados')

    def __str__(self):
        return f"Despacho de {self.arriendo.producto} a {self.arriendo.usuario} ({self.estado})"
