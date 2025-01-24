from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from django.shortcuts import render

# API Views
class CategoryListView(ListAPIView):
    queryset = Category.objects.prefetch_related('subcategories__items__sizes')
    serializer_class = CategorySerializer

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.prefetch_related('sizes')
    serializer_class = ItemSerializer

# Frontend Views
def index(request):
    categories = Category.objects.prefetch_related('subcategories__items__sizes')
    return render(request, 'index.html', {'categories': categories})

def item_detail(request, pk):
    item = Item.objects.prefetch_related('sizes').get(pk=pk)
    return render(request, 'item_detail.html', {'item': item})
