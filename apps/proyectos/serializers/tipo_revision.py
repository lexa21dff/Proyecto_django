from rest_framework import serializers
from apps.proyectos.models.tipo_revision import Tipo_Revision

class Tipo_revisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_Revision
        fields = ['url','id','nombre']

