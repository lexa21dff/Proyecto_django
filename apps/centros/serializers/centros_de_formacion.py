from rest_framework import serializers
from apps.centros.models.centros_de_formacion import Centros_de_formacion

class Centros_de_formacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Centros_de_formacion
        fields = ['url', 'id','nombre', 'regional']