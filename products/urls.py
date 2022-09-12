from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, FileListView, FileDetailView
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:product_pk>/files/', FileListView.as_view(), name='file-list'),
    path('categories/<int:product_pk>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),




]