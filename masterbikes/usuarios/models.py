from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = [
        ('CLIENTE', 'Cliente'),
        ('TECNICO', 'Técnico'),
        ('VENDEDOR', 'Vendedor'),
        ('SUPERVISOR', 'Supervisor'),
    ]

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    rol = models.CharField(max_length=15, choices=ROLES, default='CLIENTE')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'rol']

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
