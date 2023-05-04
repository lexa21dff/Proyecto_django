from django.db import models
ESTADO_PROYECTO = (
    ('terminado', 'terminado'),
    ('en revision', 'en revision'),
    ('en desarrollo', 'en desarrollo'),
)


class Proyecto(models.Model):
    nombre_proyecto     = models.CharField(max_length=300 )    
    descripcion         = models.CharField(max_length=5000 )    
    foto                = models.ImageField(upload_to='proyectos/foto', null=True, blank=True)

    codigo_fuente       = models.URLField(null= True, blank= True,)    
    categorias          = models.ManyToManyField('proyectos.Categoria', null=True, blank=True)

   
    estado              = models.CharField(max_length=20, choices = ESTADO_PROYECTO, default = 'en revision')

    creado              = models.DateTimeField(auto_now_add = True)
    editado             = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nombre_proyecto
