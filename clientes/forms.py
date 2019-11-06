from django import forms
from clientes.models import registroC

class regristoClientes(forms.ModelForm):
    class meta:
        model = registroC
        fields = '__all__'

        widgets = {
            'Nombre': forms.TextInput(attrs=none)
            'Apellido': forms.TextInput(attrs=none)
            'colonia': forms.TextInput(attrs=none)
        }