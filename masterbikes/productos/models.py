from django.db import models

# Create your models here.

class Producto(models.Model):
    TIPOS = [
        ('BICICLETA', 'Bicicleta'),
        ('ACCESORIO', 'Accesorio'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=15, choices=TIPOS)
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    rodado = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    año = models.PositiveIntegerField(blank=True, null=True)
    tipo_accesorio = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
