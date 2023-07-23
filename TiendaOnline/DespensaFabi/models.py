from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    CATEGORIAS_CHOICES = [
        ('enlatados', 'Enlatados'),
        ('bebidas', 'Bebidas'),
        ('jugos', 'Jugos'),
        ('limpieza', 'Limpieza'),
        ('comestibles', 'Comestibles'),
        ('lacteos', 'Lacteos'),
        ('cocina', 'Cocina'),
        ('fiambres', 'Fiambres'),
        ('mayoreo', 'Mayoreo'),
    ]

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES, default='comestibles')

    def __str__(self):
        return f'{self.nombre} - {self.precio}'

    class Meta:
        verbose_name_plural = "Productos"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    postal = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Usuarios"


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

    class Meta:
        verbose_name_plural = "Carrito"


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carrito}"

    class Meta:
        verbose_name_plural = "ItemCarrito"
