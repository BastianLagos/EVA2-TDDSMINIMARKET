from django.db import models

class Cliente(models.Model):
    nombre = models.TextField(max_length=50)
    rut = models.TextField(unique = True, max_length=13)
    correo = models.TextField(max_length=50)
    direccion = models.TextField(max_length=50)
    contraseña1 = models.TextField(max_length=50)
    contraseña2 = models.TextField(max_length=50)