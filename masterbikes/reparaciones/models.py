from django.db import models
from usuarios.models import Usuario
from productos.models import Producto

class Reparacion(models.Model):
    ESTADOS = [
        ('SOLICITADO', 'Solicitado'),
        ('EN_PROCESO', 'En proceso'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reparaciones')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='reparaciones')
    tecnico = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='reparaciones_asignadas')
    descripcion_problema = models.TextField()
    estado = models.CharField(max_length=15, choices=ESTADOS, default='SOLICITADO')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reparación de {self.producto} para {self.usuario} ({self.estado})"
