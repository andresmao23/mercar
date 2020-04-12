from .models import Client, Store
from rest_framework import serializers
from order.serializers import OrderSerializer

class ClientSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    class Meta:
        model = Client
        fields = ('id', 'name','first_lastname','cedula', 'orders')

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name','first_lastname','cedula')

class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        depth = 1

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'