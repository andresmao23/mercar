from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name='Cédula')
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    first_lastname = models.CharField(max_length=100, null=False, blank=False, verbose_name='Primer Apellido')
    second_lastname = models.CharField(max_length=100, null=True, blank=True, verbose_name='Segundo Apellido')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['-created']
    
    def __str__(self):
        return self.cedula
        #return self.name + ' ' + self.first_lastname

class Store(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name='Nombre del establecimiento')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Dirección')
    neighborhood = models.CharField(max_length=100, null=True, blank=True, verbose_name='Barrio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Establecimiento'
        verbose_name_plural='Establecimientos'
        ordering=['-created']
    
    def __str__(self):
        return self.name