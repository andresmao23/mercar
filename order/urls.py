from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderList, OrderProductList, OrderListClient
#from .views import OrderViewSet, OrderProductViewSet

# Create a router and register our viewsets with it.
#router = DefaultRouter()
#router.register(r'order-list-client', OrderViewSet)
#router.register(r'productsonorder', OrderProductViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    #path('', include(router.urls)),
    path('order-list/', OrderList.as_view(), name='order-list'),
    path('order-list/<int:client_id>', OrderListClient.as_view(), name='order-list-client'),
    path('orderproduct-list/', OrderProductList.as_view(), name='orderproduct-list'),
]