from django.db import models

class Producto(models.Model):
    codigo = models.TextField(unique = True, max_length=50)
    nombre = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)
    precio = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)
    imagen = models.ImageField(upload_to="imagenes_bd/", null=True, blank=True)