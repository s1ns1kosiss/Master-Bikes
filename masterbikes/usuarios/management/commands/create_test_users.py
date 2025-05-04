from django.core.management.base import BaseCommand
from usuarios.models import Usuario

class Command(BaseCommand):
    help = 'Crea usuarios de prueba para cada rol'

    def handle(self, *args, **kwargs):
        # Lista de usuarios de prueba
        test_users = [
            {
                'username': 'vendedor1',
                'email': 'vendedor1@masterbikes.com',
                'password': 'vendedor123',
                'nombre': 'Juan',
                'apellido': 'Pérez',
                'rut': '12345678-9',
                'telefono': '912345678',
                'direccion': 'Calle Comercio 123',
                'rol': 'VENDEDOR'
            },
            {
                'username': 'tecnico1',
                'email': 'tecnico1@masterbikes.com',
                'password': 'tecnico123',
                'nombre': 'Pedro',
                'apellido': 'González',
                'rut': '98765432-1',
                'telefono': '987654321',
                'direccion': 'Calle Taller 456',
                'rol': 'TECNICO'
            },
            {
                'username': 'cliente1',
                'email': 'cliente1@masterbikes.com',
                'password': 'cliente123',
                'nombre': 'María',
                'apellido': 'López',
                'rut': '11111111-1',
                'telefono': '911111111',
                'direccion': 'Avenida Principal 789',
                'rol': 'CLIENTE'
            }
        ]

        # Eliminar usuarios existentes
        for user_data in test_users:
            Usuario.objects.filter(username=user_data['username']).delete()

        # Crear nuevos usuarios
        for user_data in test_users:
            try:
                # Crear el usuario
                user = Usuario.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password'],
                    nombre=user_data['nombre'],
                    apellido=user_data['apellido'],
                    rut=user_data['rut'],
                    telefono=user_data['telefono'],
                    direccion=user_data['direccion'],
                    rol=user_data['rol']
                )
                self.stdout.write(self.style.SUCCESS(f'Usuario {user_data["username"]} creado exitosamente'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear usuario {user_data["username"]}: {str(e)}')) 