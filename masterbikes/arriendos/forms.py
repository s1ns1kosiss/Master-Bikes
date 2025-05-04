from django import forms
from .models import Arriendo
from productos.models import Producto

class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['producto', 'fecha_inicio', 'fecha_fin', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo productos disponibles
        self.fields['producto'].queryset = Producto.objects.filter(estado='DISPONIBLE')

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError('La fecha de inicio debe ser anterior a la fecha de fin.')

        return cleaned_data 