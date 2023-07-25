from django.contrib.auth.models import User, Group
from proyecto.models import Departamento, Edificio, Propietario

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    cuartos = serializers.SerializerMethodField()
    costo = serializers.SerializerMethodField()

    class Meta:
        model = Edificio
        fields = '__all__'

    def get_cuartos(self, obj):
        return obj.get_nro_cuartos_total()
    
    def get_costo(self, obj):
        return obj.get_costo_total()


class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    # Serealizamos o Codificamos un método a convertir un atributo
    departamentos = serializers.SerializerMethodField()
    edificios = serializers.SerializerMethodField()
    
    class Meta:
        model = Propietario
        fields = '__all__'

    def get_departamentos(self, obj):
        return obj.get_total_departamentos()
    
    def get_edificios(self, obj):
        return obj.get_edificios()


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
