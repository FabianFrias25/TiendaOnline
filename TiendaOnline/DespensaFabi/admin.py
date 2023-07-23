from django.contrib import admin
from DespensaFabi.models import Producto, UserProfile, Carrito, ItemCarrito


admin.site.register(Producto)
admin.site.register(UserProfile)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
