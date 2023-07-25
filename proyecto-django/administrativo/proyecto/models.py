from django.db import models

# Create your models here.
class Edificio(models.Model):
    opciones_tipo_edificio = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        ('negocio', 'Negocio'),
        ('público', 'Público')
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=opciones_tipo_edificio)

    def __str__(self):
        return "Edificio: %s - %s - %s - %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)
    
    def get_nro_cuartos_total(self):
        cantidadTotal = [d.nro_cuartos for d in self.departamentosE.all()]
        cantidadTotal = sum(cantidadTotal)
        return cantidadTotal
    
    def get_costo_total(self):
        costoTotal = [d.costo for d in self.departamentosE.all()]
        costoTotal = sum(costoTotal)
        return costoTotal


class Propietario(models.Model):
    cedula = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def get_total_departamentos(self):
        cantidadTotal = [d for d in self.departamentosP.all()]
        return len(cantidadTotal)
    
    def get_edificios(self):
        lista = [d.edificio.nombre for d in self.departamentosP.all()]
        return lista
    
    def __str__(self):
        return "Propietario: %s - %s %s" % (self.cedula, 
                self.nombre, 
                self.apellido)
    

class Departamento(models.Model):
    costo = models.IntegerField()
    nro_cuartos =  models.IntegerField("Número de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentosE")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentosP")

    def __str__(self):
        return "Departamento: %f - Num. Cuartos = %d" % (self.costo, 
                self.nro_cuartos)