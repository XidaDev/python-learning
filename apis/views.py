from django.shortcuts import render
from apis.serializers import BookSerializer

from books.models import Book
from rest_framework import generics
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer