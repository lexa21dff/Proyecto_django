from django.db import models

TIPO_DOCUMENTO = (
    ('CC', 'CC'),
    ('TI', 'TI'),
    ('CE', 'CE'),
    ('PASAPORTE', 'PASAPORTE'),
)

class Perfil(models.Model):
    """perfil model

    Un perfil contiene datos públicos de un usuario como:
    documento, tipo documento, direccion , foto ...
    """
    documento       = models.PositiveIntegerField(unique=True)
    tipo_documento  = models.CharField(max_length=20, choices = TIPO_DOCUMENTO)
    direccion       = models.CharField(max_length=50,null= True, blank= True)
    telefono        = models.CharField(max_length=15,null= True, blank= True)
    foto            = models.ImageField(upload_to='perfiles', null=True, blank=True)
    web             = models.URLField(null= True, blank= True,)
    rol             = models.ForeignKey('users.Rol',on_delete = models.PROTECT)
    usuario         = models.OneToOneField('users.User', on_delete = models.CASCADE)
    creado          = models.DateTimeField(auto_now_add = True)
    editado         = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.usuario.username 