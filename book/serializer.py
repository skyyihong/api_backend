from rest_framework.serializers import ModelSerializer
from book.models import Book


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', "author", "price", "stock", "sold"]
