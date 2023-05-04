from django.db import models

ROL = (
    ('aprendiz', 'Aprendiz'),
    ('instructor', 'Instructor'),
    ('admin', 'Admin'),
    ('anonimo', 'Anonimo'),
)

class Rol(models.Model):
    nombre  = models.CharField(max_length=30, choices=ROL, unique=True)
    
    def __str__(self):
        return self.nombre