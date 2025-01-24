from rest_framework import serializers
from .models import Category, SubCategory, Item, Size

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name', 'price']

class ItemSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'image', 'sizes']

class SubCategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'items']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategories']
