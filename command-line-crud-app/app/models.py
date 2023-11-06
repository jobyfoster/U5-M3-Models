from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_date = models.DateField()
    publisher = models.CharField(max_length=255)
    num_of_pages = models.PositiveIntegerField()


def create_book(name, author, release_date, publisher, num_of_pages):
    book = Book.objects.create(
        name=name,
        author=author,
        release_date=release_date,
        publisher=publisher,
        num_of_pages=num_of_pages,
    )

    return book


def all_books():
    return Book.objects.all()


def find_book_by_name(name):
    try:
        return Book.objects.get(name=name)
    except Book.DoesNotExist:
        return None


def find_books_longer_than(pages):
    return Book.objects.filter(num_of_pages__gt=pages)


def update_book_name(name, new_name):
    book = Book.objects.get(name=name)
    book.name = new_name
    book.save()


def delete_book(name):
    Book.objects.get(name=name).delete()
