from django.db import models
from usuarios.models import Usuario
from productos.models import Producto

class Arriendo(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('EN_CURSO', 'En curso'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='arriendos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='arriendos')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=15, choices=ESTADOS, default='RESERVADO')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    entregado = models.BooleanField(default=False)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    fecha_devolucion_real = models.DateTimeField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=30, blank=True, null=True)
    descuento_aplicado = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Arriendo de {self.producto} por {self.usuario} ({self.estado})"
