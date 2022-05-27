from django.urls import path
from . import views


urlpatterns = [
    path('products', views.products_view, name='products'),
    path('products/<str:pk>', views.product_detail_view, name='product-detail'),
    path('create-product', views.create_product, name='create-product'),
    path('update-product/<str:pk>', views.update_product, name='update-product'),
    path('delete-product/<str:pk>', views.delete_product, name='delete-product'),
    path('delete-comment/<str:pk>', views.delete_comment, name='delete-comment')
]