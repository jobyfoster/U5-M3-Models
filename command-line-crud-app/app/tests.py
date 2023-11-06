from django.test import TestCase
from django.core.exceptions import ValidationError
from app.models import (
    Book,
    create_book,
    all_books,
    find_book_by_name,
    find_books_longer_than,
    update_book_name,
    delete_book,
)
from datetime import date


class TestBook(TestCase):
    def test_can_create_book(self):
        book = create_book(
            "Django for Beginners",
            "William S. Vincent",
            date(2018, 12, 25),
            "DjangoBooks Publishing",
            200,
        )

        self.assertIsNotNone(book.id)
        self.assertEqual(book.name, "Django for Beginners")
        self.assertEqual(book.author, "William S. Vincent")
        self.assertEqual(book.release_date, date(2018, 12, 25))
        self.assertEqual(book.publisher, "DjangoBooks Publishing")
        self.assertEqual(book.num_of_pages, 200)

    def test_can_view_all_books_at_once(self):
        books_data = [
            {
                "name": "Two Scoops of Django",
                "author": "Audrey R. Greenfeld",
                "release_date": date(2019, 5, 1),
                "publisher": "Two Scoops Press",
                "num_of_pages": 300,
            },
            {
                "name": "Lightweight Django",
                "author": "Julia Elman",
                "release_date": date(2015, 11, 11),
                "publisher": "O'Reilly Media",
                "num_of_pages": 250,
            },
        ]

        for book_data in books_data:
            create_book(
                book_data["name"],
                book_data["author"],
                book_data["release_date"],
                book_data["publisher"],
                book_data["num_of_pages"],
            )

        books = all_books()

        self.assertEqual(len(books), len(books_data))

        books_data_sorted = sorted(books_data, key=lambda b: b["name"])
        books_sorted = sorted(books, key=lambda b: b.name)

        for data, book in zip(books_data_sorted, books_sorted):
            self.assertEqual(data["name"], book.name)
            self.assertEqual(data["author"], book.author)
            self.assertEqual(data["release_date"], book.release_date)
            self.assertEqual(data["publisher"], book.publisher)
            self.assertEqual(data["num_of_pages"], book.num_of_pages)

    def test_can_find_book_by_name(self):
        create_book(
            "Django Unleashed",
            "Andrew Pinkham",
            date(2015, 12, 1),
            "Sams Publishing",
            840,
        )

        self.assertIsNone(find_book_by_name("Nonexistent Book"))

        book = find_book_by_name("Django Unleashed")

        self.assertIsNotNone(book)
        self.assertEqual(book.author, "Andrew Pinkham")

    def test_can_find_books_longer_than(self):
        create_book(
            "Django Unleashed",
            "Andrew Pinkham",
            date(2015, 12, 1),
            "Sams Publishing",
            840,
        )

        self.assertEqual(len(find_books_longer_than(500)), 1)

    def test_can_update_book_name(self):
        book = create_book(
            "Mastering Django", "Nigel George", date(2016, 7, 28), "Nigel George", 524
        )

        update_book_name("Mastering Django", "Mastering Django: Core")

        updated_book = find_book_by_name("Mastering Django: Core")
        self.assertIsNotNone(updated_book)
        self.assertEqual(updated_book.author, "Nigel George")

    def test_can_delete_book(self):
        create_book(
            "Django for APIs",
            "William S. Vincent",
            date(2019, 6, 30),
            "DjangoBooks Publishing",
            250,
        )

        delete_book("Django for APIs")

        self.assertIsNone(find_book_by_name("Django for APIs"))
