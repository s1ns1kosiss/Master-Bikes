from django.db import models
from productos.models import Producto
from usuarios.models import Usuario

class Promocion(models.Model):
    TIPOS_CLIENTE = [
        ('TODOS', 'Todos'),
        ('CLIENTE', 'Cliente'),
        ('TECNICO', 'Técnico'),
        ('VENDEDOR', 'Vendedor'),
        ('SUPERVISOR', 'Supervisor'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipo_cliente = models.CharField(max_length=15, choices=TIPOS_CLIENTE, default='TODOS')
    productos = models.ManyToManyField(Producto, blank=True, related_name='promociones')
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuarios_destinatarios = models.ManyToManyField(Usuario, blank=True, related_name='promociones_recibidas')

    def __str__(self):
        return f"{self.titulo} ({self.tipo_cliente})"
