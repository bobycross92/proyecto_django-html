from django.db import models

# Create your models here.
from django.db import models

# CLIENTE
class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    cul_nombre = models.CharField(max_length=50)
    cul_apellido = models.CharField(max_length=50)
    cul_correo = models.CharField(max_length=50)
    cul_telefono = models.CharField(max_length=15)
    cul_direccion = models.CharField(max_length=100)
    cul_region = models.CharField(max_length=50)
    cul_postal = models.CharField(max_length=10)
    cul_pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cul_nombre} {self.cul_apellido}"

# ORDEN
class Orden(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ord_fecha = models.DateField()

    def __str__(self):
        return f"Orden #{self.id_orden}"

# PRODUCTO
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    cat_nombre = models.CharField(max_length=50)
    cat_foto = models.BinaryField(null=True, blank=True)

class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    prv_nombre = models.CharField(max_length=50)
    prv_contacto = models.CharField(max_length=50)
    prv_correo = models.CharField(max_length=50)
    prv_telefono = models.CharField(max_length=15)
    prv_direccion = models.CharField(max_length=100)
    prv_region = models.CharField(max_length=50)
    prv_postal = models.CharField(max_length=10)
    prv_pais = models.CharField(max_length=50)

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    pro_nombre = models.CharField(max_length=50)
    pro_precio = models.DecimalField(max_digits=8, decimal_places=2)
    pro_stock = models.IntegerField()

    def __str__(self):
        return self.pro_nombre

# DETALLE ORDEN
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    deg_cantidad = models.IntegerField()

# EMPLEADO
class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    emp_nombre = models.CharField(max_length=50)
    emp_apellido = models.CharField(max_length=50)
    emp_correo = models.CharField(max_length=50)
    emp_telefono = models.CharField(max_length=15)
    emp_direccion = models.CharField(max_length=100)
    emp_fecha_contrato = models.DateField()
    emp_fecha_nacimiento = models.DateField()
    emp_foto = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"{self.emp_nombre} {self.emp_apellido}"
