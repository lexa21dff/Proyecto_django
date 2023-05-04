from django.db import models
class Grupo (models.Model):
    nombre_grupo    = models.CharField(max_length=15, unique = True) # c+odigo auto generado por medio de un script 

    def __str__(self):
        return self.nombre_grupo