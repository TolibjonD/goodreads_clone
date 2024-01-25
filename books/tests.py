from django.test import TestCase
from books.models import Book
from django.urls import reverse

# Create your tests here.
class BooksTestCase(TestCase):
    def test_not_found(self):
        res = self.client.get(
            reverse("books:books")
        )

        self.assertContains(res, "No books found 😔")

    def test_books_created(self):
        Book.objects.create(title = "title1" , description = "descr1" , isbn="isbn1")
        Book.objects.create(title = "title2" , description = "descr2" , isbn="isbn2")
        Book.objects.create(title = "title3" , description = "descr3" , isbn="isbn3")

        res = self.client.get(
            reverse("books:books")
        )

        books = Book.objects.all()
        for book in books:
            self.assertContains(res , book.title)

    def test_books_detail(self):
        book = Book.objects.create(title = "title1" , description="description" , isbn="isbn-123")

        response = self.client.get(
            reverse("books:detail", kwargs={"id": book.id})
        )

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

