from django.urls import include, path
from rest_framework import routers

from apps.proyectos.views.tipo_revision import *
from apps.proyectos.views.categoria import *
from apps.proyectos.views.proyecto import *
from apps.proyectos.views.entrega import *
from apps.proyectos.views.documento import *

router = routers.DefaultRouter()

router.register(r'tipo_revision', Tipo_revisionViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'proyecto', ProyectoViewSet)
router.register(r'entrega', EntregaViewSet)
router.register(r'documento', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]