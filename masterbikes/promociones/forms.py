from django import forms
from .models import Promocion

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = [
            'titulo',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'descuento',
            'tipo_cliente',
            'productos',
            'usuarios_destinatarios'
        ]
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'productos': forms.SelectMultiple(attrs={'class': 'select2'}),
            'usuarios_destinatarios': forms.SelectMultiple(attrs={'class': 'select2'})
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise forms.ValidationError(
                "La fecha de inicio debe ser anterior a la fecha de fin."
            )

        return cleaned_data 