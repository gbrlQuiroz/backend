from django.db import models


class Usuario(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=150)

    class Meta:
        db_table = 'usuarios'
        ordering = ['-id']


class ExtraInfo(models.Model):
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True, db_column='fecha_nacimiento')
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='extraInfo')

    class Meta:
        db_table = 'informacion_extra'
