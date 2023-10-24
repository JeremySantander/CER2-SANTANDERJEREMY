from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

TIPO_CHOICES = [
    ("S", "Suspension de actividades"),
    ("C", "Suspension de clase"),
    ("I", "Informacion")]

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=75)
    logo = models.ImageField(upload_to='core/static/core/img/Logo Entidad/', verbose_name='LogoArticulo')

    def __str__(self) -> str:
        return self.nombre
    
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=75)
    detalle = models.CharField(max_length=700)
    detalle_corto = models.CharField(max_length=45)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default = 'S')
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = User
    modificado_por = User

    def __str__(self) -> str:
        return self.titulo
    