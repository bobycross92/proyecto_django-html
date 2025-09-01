from django.contrib import admin
from .models import (
    Cliente,
    Orden,
    DetalleOrden,
    Producto,
    Empleado,
    Categoria,
    Proveedor
)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cli_nombre', 'cli_correo')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'ord_fecha')

class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'deg_cantidad')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pro_nombre', 'pro_precio')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('emp_nombre', 'emp_fecha_contrato')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'cat_nombre')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('prv_nombre', 'prv_correo')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(DetalleOrden, DetalleOrdenAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
