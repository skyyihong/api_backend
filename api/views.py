from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializer import BookModelSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class BookModelViewSet(ModelViewSet):
    # authentication_classes = [JSONWebTokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
