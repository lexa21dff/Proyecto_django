from rest_framework import serializers
from apps.proyectos.models import Documento

class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Documento
        fields = ['url', 'id','documento','entrega']
