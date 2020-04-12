from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderProductSerializer, OrderPOSTSerializer
from .models import Order, OrderProduct

# Create your views here.

'''class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        print (data)'''
    
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderPOSTSerializer

class OrderListClient(generics.ListAPIView):
    serializer_class =   OrderSerializer
    def get_queryset(self):
        #print(self.kwargs['client_id'])
        client_id = self.kwargs['client_id']
        return Order.objects.filter(client_id=client_id)

class OrderProductList(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def post(self, request, *args, **kwargs):
        #print(request.data)
        for elem in request.data:
            serializer = OrderProductSerializer(data=elem)
            if serializer.is_valid():
                serializer.save()
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(request.data, status=status.HTTP_201_CREATED)