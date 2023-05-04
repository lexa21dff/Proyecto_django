from django.db import models

class Programa(models.Model):
    nombre               = models.CharField(max_length=300,unique=True)
    centrosDeFormacion = models.ForeignKey('centros.centros_de_formacion', on_delete=models.PROTECT) 
    # Centros de formacion tiene una relacion de UNO a MUCHOS con Programa
       
    def __str__(self):
        return self.nombre