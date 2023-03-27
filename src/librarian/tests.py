from django.test import TestCase, Client
from django.shortcuts import reverse


from .models import Book, Reader, Borrowing

# Create your tests here.

class BorrowingTest(TestCase):
    def setUp(self):
        book = Book(
            title='Baśnie', author_name='Hans', author_surname='Andersen'
        )
        book.save()
        reader = Reader(
            name='Alicja', surname='Malinowska'
        )
        reader.save()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_borrow_form(self):
        session = self.client.session
        session['reader_id'] = 1
        session.save()
        response = self.client.post(reverse('borrow-book'), data={'id': 1})
        print(response)
