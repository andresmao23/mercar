from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductByCategoryList, ProductDetail
#from .views import CategoryList, ProductList, CategoryDetailAPIView, ProductDetailAPIView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product-list', ProductViewSet)
router.register(r'category-list', CategoryViewSet)
#router.register(r'product_by_category/(?P<category_id>[0-9]+)/$', ProductByCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-by-category/<int:id>', ProductByCategoryList.as_view(), name='product-by-category'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    #path('category-list/', CategoryList.as_view(), name='category-list'),
    #path('category/<slug:name>', CategoryDetailAPIView.as_view(), name='category-detail'),
    #path('product-list/', ProductList.as_view(), name='product-list'),
    #path('product/<slug:name>', ProductDetailAPIView.as_view(), name='product-detail'),
]