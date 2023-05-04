from rest_framework import serializers
from apps.centros.models.ficha import Ficha

class FichaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ficha
        fields = ['url','id', 'codigo', 'programa', 'fecha_inicio', 'fecha_finalizacion']

