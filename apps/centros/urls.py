from django.urls import include, path
from rest_framework import routers

# Centros de formacion
from apps.centros.views.regional import *
from apps.centros.views.ficha import *
from apps.centros.views.centros_de_formacion import *
from apps.centros.views.programa import *

router = routers.DefaultRouter()

# Centros de formacion
router.register(r'regional', RegionalViewSet)
router.register(r'ficha', FichaViewSet)
router.register(r'centro', Centros_de_formacionViewSet )
router.register(r'programa', ProgramaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]