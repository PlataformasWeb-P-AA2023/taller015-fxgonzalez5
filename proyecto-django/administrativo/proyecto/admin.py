from django.contrib import admin

# Register your models here.
from proyecto.models import Edificio, Departamento, Propietario

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad', 'tipo')

admin.site.register(Edificio, EdificioAdmin)


class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido')
    search_fields = ('cedula', 'nombre', 'apellido')

admin.site.register(Propietario, PropietarioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('get_propietario', 'costo', 'nro_cuartos', 'get_edificio')
    search_fields = ('costo', 'nro_cuartos')
    raw_id_fields = ('edificio', 'propietario')

    def get_edificio(self, obj):
        """ """
        return obj.edificio.nombre
    
    def get_propietario(self, obj):
        """ """
        return obj.propietario.nombre

admin.site.register(Departamento, DepartamentoAdmin)
