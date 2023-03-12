from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    author_surname = models.CharField(max_length=100)


class Reader(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Borrowing(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    
