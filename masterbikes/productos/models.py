from django.db import models

# Create your models here.

class Producto(models.Model):
    TIPOS = [
        ('BICICLETA', 'Bicicleta'),
        ('ACCESORIO', 'Accesorio'),
    ]

    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('EN_REPARACION', 'En reparación'),
        ('NO_DISPONIBLE', 'No disponible'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=15, choices=TIPOS)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='DISPONIBLE')
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    rodado = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    tipo_accesorio = models.CharField(max_length=50, blank=True, null=True)
    imagen_url = models.URLField('Imagen (URL)', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
