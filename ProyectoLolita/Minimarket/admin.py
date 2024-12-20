from django.contrib import admin

from Minimarket.models import Producto, Compra, Cliente

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','codigo','nombre','tipo','precio','cantidad','imagen']

class CompraAdmin(admin.ModelAdmin):
    list_display = ['id','codigo','nombre','precio']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','rut','correo','direccion','contraseña1','contraseña2']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Cliente, ClienteAdmin)