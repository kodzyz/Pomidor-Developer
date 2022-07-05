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
    # настройка фильтрации через API , filter_fields, DjangoFilterBackend
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [
        IsAuthenticated]  # https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
    filterset_fields = ['price']  # http://127.0.0.1:8000/book/?price=1000
    # настройка поиска через search_fields в API View , SearchFilter
    search_fields = ['name', 'author_name']  # http://127.0.0.1:8000/book/?search=Hemingway
    # Ordering в Django REST Framework, OrderingFilter, ordering_fields
    ordering_fields = ['price', 'author_name']  # http://127.0.0.1:8000/book/?ordering=price


def auth(request):
    return render(request, 'oauth.html')
