from django.db import models

class Tipo_Revision(models.Model):
    nombre      = models.CharField(max_length=200, unique = True)

    def __str__(self):
        return self.nombre