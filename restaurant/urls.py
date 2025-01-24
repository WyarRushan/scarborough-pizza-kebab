from django.urls import path
from .views import CategoryListView, ItemDetailView, index, item_detail

urlpatterns = [
    path('', index, name='index'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/<int:pk>/', item_detail, name='item-detail-view'),
]