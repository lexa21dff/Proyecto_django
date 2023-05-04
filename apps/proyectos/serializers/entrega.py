from rest_framework import serializers
from apps.proyectos.models.entrega import Entrega

class EntregaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrega
        fields = ['url', 'id','calificacion', 'descripcion_entrega','respuesta_instructor','proyecto','aprendiz','creado', 'editado']
