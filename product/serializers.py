from .models import Category, Product
from rest_framework import serializers
from order.serializers import OrderProductSerializer
from order.models import OrderProduct

class ProductSerializer(serializers.ModelSerializer):
    orderproducts = OrderProductSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description', 'price', 'category_id', 'stock','orderproducts')

class ProductByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description', 'price', 'category_id', 'stock')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name','image','description')

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description', 'price', 'category_id', 'stock')