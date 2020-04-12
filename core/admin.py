from django.contrib import admin
from .models import Client, Store

# Register your models here.

admin.site.site_header='Tenderos Online'
admin.site.index_title='Panel de administración'
admin.site.site_title='Tenderos Online'

class ClientAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated',)
    list_display = ('name','first_lastname', 'second_lastname','created',)
    search_fields = ['cedula','name','first_lastname']
    list_filter = ['created']

class StoreAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated',)
    list_display = ('name','created',)
    search_fields = ['name','client_id__cedula','client_id__name','client_id__first_lastname']
    list_filter = ['created']

admin.site.register(Client, ClientAdmin)
admin.site.register(Store, StoreAdmin)