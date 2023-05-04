from django.db import models

MODALIDAD = (
    ('presencial', 'Presencial'),
    ('virtual', 'Virtual'),
)

class Ficha(models.Model):

    codigo              = models.PositiveIntegerField(unique=True) 
    fecha_inicio        = models.DateField()
    fecha_finalizacion  = models.DateField()
    modalidad           = models.CharField(max_length=12, choices = MODALIDAD, default='presencial') # Presencial o Virtual
    programa            = models.ForeignKey('centros.Programa', on_delete = models.PROTECT) 
    # Programa tiene una relacion de uno a muchos con Ficha(programa)
    
    def __str__(self):
        return str(self.codigo) + " " + self.programa.nombre