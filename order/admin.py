from django.contrib import admin
from django.shortcuts import render
from django.core import serializers
from .models import Order, OrderProduct
from core.models import Client, Store
from product.models import Product, Category
from .serializers import OrderSerializer
import pandas as pd #Librería pandas para hacer el consolidado de acuerdo al nombre de producto y categoría

# Register your models here.
# Método que ordena los pedidos de acuerdo a su categoría
def getCategory(item):
    return item['categoria']

class OrderAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated',)
    list_display = ('id','created',)
    search_fields = ['id','client_id__name','client_id__first_lastname','client_id__cedula']
    list_filter = ['created']

    def consultar_pedido(self, request, queryset):
        template = 'admin/orden.html'
        #lista = []
        clientes = queryset
        tam = len(clientes)
        ced = clientes[0].client_id
        cliente = Client.objects.filter(cedula=ced).values('id','cedula', 'name', 'first_lastname', 'phone')
        establecimiento = {}
        try:
            establecimiento = Store.objects.get(client_id=cliente[0]['id'])
        except:
            print("No existe el establecimiento o el cliente tiene más de uno!")
        #print(establecimiento.name)
        #print(establecimiento.address)
        #print(establecimiento.neighborhood)
        #print (cliente[0])
        #print(tam)
        total = 0
        for orden in queryset:
            #print(orden.id)
            query = OrderProduct.objects.filter(order_id=orden.id).values('product_id__name', 'product_id', 'quantity', 'product_id__price')
            #lista.append(query)
        #print(lista)
        for q in query:
            #print (q['quantity'])
            total = total + (q['quantity']*q['product_id__price'])
        #print(total)
        context = {'lista_orden': query, 'clientes':clientes, 'cliente':cliente[0], 'tamano':tam, 'total':total, 'establecimiento':establecimiento}
        return render(request, template, context)
    
    consultar_pedido.short_description = "Consultar pedido (Generar factura)"
    actions = [consultar_pedido]


class OrderProductAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated',)
    list_display = ('order_id','product_id','quantity','created',)
    #search_fields = ['order_id']
    list_filter = ['created']

    def consultar_consolidado(self, request, queryset):
        productos = []
        productos_ordenados = []
        template = 'admin/consolidado.html'        
        for q in queryset:
            product = Product.objects.get(name=q.product_id)
            p = {}
            p['nombre'] = str(q.product_id)
            p['cantidad'] = q.quantity
            p['categoria'] = str(product.category_id)
            productos.append(p)
        productos_ordenados = sorted(productos, key=getCategory)

        #Uso de pandas para obtener la suma de los productos de acuerdo a su nombre y categoría
        df = pd.DataFrame(productos_ordenados)
        lista_prod = df.groupby(("nombre", "categoria")).sum().reset_index().to_dict(orient="records")
        #print(lista_productos)
        lista_productos = sorted(lista_prod, key=lambda k: k['categoria'])
        #print(lista_ord)

        context = {'lista_productos': lista_productos}
        return render(request, template, context)
    
    consultar_consolidado.short_description = "Consultar consolidado"
    actions = [consultar_consolidado]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)