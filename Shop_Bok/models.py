from django.urls import reverse
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Shop(models.Model):
    Name1 = models.CharField(max_length=100)
    Adress = models.CharField(max_length=100)
    books = models.ManyToManyField('Book')

    def get_absolute_url(self):
        return reverse('shop-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.Name1, self.Adress)
