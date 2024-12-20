from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.TextField(unique = True, max_length=50)
    nombre = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)
    precio = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)
    imagen = models.ImageField(upload_to="imagenes_bd/", null=True, blank=True)

class Compra(models.Model):
    codigo = models.TextField(max_length=50)
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField(null=False)

class Cliente(models.Model):
    nombre = models.TextField(max_length=50)
    rut = models.TextField(unique = True, max_length=13)
    correo = models.TextField(max_length=50)
    direccion = models.TextField(max_length=50)
    contraseña1 = models.TextField(max_length=50)
    contraseña2 = models.TextField(max_length=50)