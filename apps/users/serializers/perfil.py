from rest_framework import serializers
from apps.users.models.perfil import Perfil
# from django.contrib.auth.models import User 

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = [ 'url','id','documento', 'rol', 'usuario']

