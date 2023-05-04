from rest_framework import serializers
from apps.centros.models.programa import Programa

class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ['url','id', 'nombre', 'centros_de_formacion']

