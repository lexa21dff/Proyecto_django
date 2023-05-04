from django.db import models


CALIFICACION = (
    ('aprobado', 'Aprobado'),
    ('desaprobado', 'desaprobado'),
)

class Entrega (models.Model):
    calificacion            = models.CharField(max_length=20, choices = CALIFICACION,null= True, blank= True)
    descripcion_entrega     = models.CharField(max_length=5000 )    
    respuesta_instructor    = models.CharField(max_length=5000, null= True, blank= True)
    instructror             = models.EmailField(null= True, blank= True)  # correo electronico del instructor que  califica la entrega
    # instructor              = models.CharField(max_length=300 ,null= True, blank= True) # solo va el nombre del instructor que hizo la revision     
    
    proyecto                = models.ForeignKey('proyectos.Proyecto', on_delete = models.PROTECT )
    tipo_revision           = models.ForeignKey('proyectos.Tipo_Revision', on_delete = models.PROTECT)
    aprendiz                = models.ForeignKey('grupos.Inscrito', on_delete=models.CASCADE)

    creado                  = models.DateTimeField(auto_now_add = True)
    editado                 = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.calificacion + " " + str(self.creado) + " " + str(self.editado)