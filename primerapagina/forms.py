from django.forms import ModelForm
from django import forms
from .models import Orden

class OrdenForm(ModelForm):
    class Meta:
        model=Orden
        fields=[
                'id_de_orden',
                'nombre',
                'correo',
                'metodo'
        ]