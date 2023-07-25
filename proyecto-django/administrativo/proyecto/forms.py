from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
 
from proyecto.models import *

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del edificio'),
            'direccion': _('Ingrese la dirección'),
            'ciudad': _('Ingrese la ciudad de locación'),
            'tipo': _('Seleccione el tipo de edificio'),
        }


    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']

        if valor[0:1] == "L":
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con L")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'nro_cuartos', 'edificio']
        labels = {
            'propietario': _('Ingrese los nombres del propietario'),
            'costo': _('Ingrese el costo del departamento'),
            'nro_cuartos': _('Ingrese el número de cuartos'),
            'edificio': _('Seleccione el edificio al que pertenece'),
        }

    def clean_costo(self):
        valor = self.cleaned_data['costo']

        if valor > 100000.00:
            raise forms.ValidationError("El costo no debe sobrepasar los $100 mil")
        return valor
    
    def clean_nro_cuartos(self):
        valor = self.cleaned_data['nro_cuartos']

        if valor == 0:
            raise forms.ValidationError("El numero de cuartos no puede ser 0")
        
        if valor > 7 :
            raise forms.ValidationError("Ha excedido el número de cuartos, no debe ser mayor a 7")
        return valor
    
    def clean_propietario (self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese el nombre completo del propietario porfavor")
        return valor
    

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'nro_cuartos', 'edificio']

    def clean_costo(self):
        valor = self.cleaned_data['costo']

        if valor > 100000.00:
            raise forms.ValidationError("El costo no debe sobrepasar los $100 mil")
        return valor
    
    def clean_nro_cuartos(self):
        valor = self.cleaned_data['nro_cuartos']

        if valor == 0:
            raise forms.ValidationError("El numero de cuartos no puede ser 0")
        
        if valor > 7 :
            raise forms.ValidationError("Ha excedido el número de cuartos, no debe ser mayor a 7")
        return valor
    
    def clean_propietario (self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese el nombre completo del propietario porfavor")
        return valor