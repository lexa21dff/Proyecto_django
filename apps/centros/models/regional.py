from django.db import models

class Regional (models.Model):
    nombre          =models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.nombre