from django.db import models
from core.models import Client
from product.models import Product

# Create your models here.
class Order(models.Model):
    STATES = (
        ('N', 'No confirmado'),
        ('C', 'Confirmado'),
    )

    client_id = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    #total = models.FloatField(default=0)
    state = models.CharField(max_length=1, choices=STATES, default='N', verbose_name='Estado del pedido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['-created']
    
    def __str__(self):
        return str(self.id)

class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, related_name='ordersprod', verbose_name='Id del pedido', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='orderproducts', verbose_name='Id del producto', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Consolidado'
        verbose_name_plural='Consolidados'
        ordering=['-created']
    
    def __str__(self):
        return str(self.order_id)