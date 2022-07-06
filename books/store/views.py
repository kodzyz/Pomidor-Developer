# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [
        IsAuthenticated]
    filterset_fields = ['price']  # http://127.0.0.1:8000/book/?price=1000
    search_fields = ['name', 'author_name']  # http://127.0.0.1:8000/book/?search=Hemingway
    ordering_fields = ['price', 'author_name']  # http://127.0.0.1:8000/book/?ordering=price


def auth(request):
    return render(request, 'oauth.html')
