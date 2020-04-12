from .models import Order, OrderProduct
from product.models import Product
from rest_framework import serializers

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'quantity','order_id', 'product_id')

class OrderProductGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'quantity', 'product_id')
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    #ordersprod = OrderProductSerializer(many=True)
    ordersprod = OrderProductGETSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id','state', 'client_id','created','ordersprod')

class OrderPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','state', 'client_id')