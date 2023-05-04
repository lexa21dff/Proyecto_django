from django.db import models


class Centros_de_formacion(models.Model):
    nombre          =models.CharField(max_length=300, unique=True)
    direccion       =models.CharField(max_length=100,null= True, blank= True )
    encargado       =models.CharField(max_length=20,null= True, blank= True)
    regional        =models.ForeignKey('centros.Regional', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + " " + self.regional.nombre
    