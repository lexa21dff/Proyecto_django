from rest_framework import serializers
from apps.proyectos.models.proyecto import Proyecto

class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['url', 'id','nombre_proyecto','descripcion', 'foto', 'codigo_fuente', 'categorias', 'estado']
