from rest_framework import serializers
from apps.centros.models.regional import Regional

class RegionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regional
        fields = ['url', 'id','nombre']

