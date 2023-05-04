from rest_framework import serializers
from apps.proyectos.models.categoria import Categoria

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['url','id', 'nombre']
