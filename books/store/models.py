from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255, default='author')

    # определяем __str__  через F-strings в python
    def __str__(self):
        return f'Id {self.id}: {self.name}'



# ./manage.py shell
# In [1]: from store.models import Book
#
# In [2]: Book.objects.all()
# Out[2]: <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
#
# In [3]: Book.objects.all()[0].price
# Out[3]: Decimal('1000.00')
#
# In [4]: Book.objects.all()[1].price
# Out[4]: Decimal('1000.00')
#
# In [5]: Book.objects.create(name='Perfume', price='500.00')


# http://127.0.0.1:8000/book/?price=500 -> [{"id":3,"name":"Perfume","price":"500.00"}]


