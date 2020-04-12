from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name='Nombre de la categoría')
    image = models.ImageField(verbose_name='Imagen', upload_to='categorys')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
        ordering=['-created']
    
    def __str__(self):
        return self.name

class Product(models.Model):

    STOCK = (
        ('D', 'Disponible'),
        ('A', 'Agotado'),
    )

    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name='Nombre del producto')
    image = models.ImageField(verbose_name='Imagen', upload_to='products')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción (Máximo 40 caracteres.)')
    price = models.FloatField(verbose_name='Precio unitario')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.CharField(max_length=1, choices=STOCK, default='D', verbose_name='Stock')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering=['-created']
    
    def __str__(self):
        return self.name
