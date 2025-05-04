from django import forms
from .models import Reparacion
from productos.models import Producto
from usuarios.models import Usuario

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = ['producto', 'descripcion_problema', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'descripcion_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo productos disponibles
        self.fields['producto'].queryset = Producto.objects.all()

class ReparacionStaffForm(ReparacionForm):
    class Meta(ReparacionForm.Meta):
        fields = ReparacionForm.Meta.fields + ['tecnico', 'costo', 'estado']
        widgets = {
            **ReparacionForm.Meta.widgets,
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo técnicos
        self.fields['tecnico'].queryset = Usuario.objects.filter(rol='TECNICO') 