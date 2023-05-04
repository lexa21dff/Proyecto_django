from  django.db import models

class Inscrito (models.Model):
    estado        = models.CharField(max_length=30)
    nombre_grupo        = models.ForeignKey('grupos.Grupo', on_delete = models.PROTECT)
    perfil          = models.ForeignKey('users.Perfil', on_delete = models.PROTECT)
    ficha           = models.ForeignKey('centros.Ficha', on_delete = models.PROTECT)
    proyecto        = models.IntegerField(null= True, blank= True) # consulta el id del Proyecto
    
    def __str__(self):
        return self.nombre_grupo