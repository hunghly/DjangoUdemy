from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # selects the model and then the fields to be serialized 
        model = Book
        fields = ['id', 'title', 'description', 'price', 'is_book_published', 'published']