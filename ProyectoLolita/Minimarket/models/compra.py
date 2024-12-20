from django.db import models

class Compra(models.Model):
    codigo = models.TextField(unique = True, max_length=50)
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField(null=False)
