from django.db import models

class Documento (models.Model):
    documento       = models.FileField(upload_to = 'proyectos/documentos',)
    entrega         = models.ForeignKey('proyectos.Entrega', on_delete=models.CASCADE)
    
    creado          = models.DateTimeField(auto_now_add = True)
    editado         = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.entrega.tipo_revision.nombre
