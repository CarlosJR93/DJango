# usuarios/forms.py
from django import forms
from datetime import datetime
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento:
            edad = (datetime.now().date() - fecha_nacimiento).days // 365
            if edad < 18:
                raise forms.ValidationError("Debes ser mayor de edad para registrarte.")
        return fecha_nacimiento
