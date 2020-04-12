from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientList, ClientUserList, ClientDetailList, StoreDetail

# Create a router and register our viewsets with it.
#router = DefaultRouter()
#router.register(r'client-list', ClientViewSet)
#router.register(r'productsonorder', OrderProductViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('login/', ClientUserList.as_view(), name='login'),
    #path('', include(router.urls)),
    #path('client-list/', ClientDetailList.as_view(), name='client-list'),
    path('client-detail/<int:id>', ClientDetailList.as_view(), name='client-detail'),
    path('store-detail/<int:client_id>', StoreDetail.as_view(), name='store-detail'),
]