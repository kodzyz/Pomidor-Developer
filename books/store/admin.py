from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from .models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
