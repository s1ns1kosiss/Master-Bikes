from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    """Formulario para el registro de nuevos usuarios."""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    rut = forms.CharField(max_length=12, required=True, label='RUT')
    telefono = forms.CharField(max_length=15, required=True, label='Teléfono')
    direccion = forms.CharField(max_length=200, required=True, label='Dirección')

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'rut', 
                 'telefono', 'direccion', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.rut = self.cleaned_data['rut']
        user.telefono = self.cleaned_data['telefono']
        user.direccion = self.cleaned_data['direccion']
        if commit:
            user.save()
        return user

class EditarPerfilForm(forms.ModelForm):
    """Formulario para editar el perfil del usuario."""
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'telefono', 'direccion', 'avatar')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'avatar': 'Foto de perfil'
        } 