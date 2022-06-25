from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)

# ./manage.py shell
# In [1]: from store.models import Book
#
# In [2]: Book.objects.create(name='For Whom The Bell Tolls', price='1000.00')
# Out[2]: <Book: Book object (1)>
#
# In [3]: Book.objects.create(name='The Collector', price='1000.00')
# Out[3]: <Book: Book object (2)>

