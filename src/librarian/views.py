import logging
logging.basicConfig(level=logging.INFO)

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import (TemplateView, )
from django.views.generic.edit import FormView

from .forms import (IdReaderForm, IdBookForm)
from .models import (Reader, Book, Borrowing)

# Create your views here.

class LibrarianView(View):
    def get(self, request):
        ctx = {
            'id_reader_form': IdReaderForm()
        }
        return render(request, 'librarian/index.html', context=ctx)

class SearchView(View):
    def get(self, request):
        return render(request, 'librarian/search.html')


class BookReturnView(View):
    def get(self, request):
        return render(request, 'librarian/return_book.html')


class ReaderProfileView(View):
    READER_NOT_FOUND = -1
    def get(self, request):
        logging.info(request.session['reader_id'])
        return render(request, 'librarian/reader.html')

    def post(self, request):
        form = IdReaderForm(request.POST)
        if form.is_valid():
            reader_id = form.cleaned_data['id']
            try:
                reader = Reader.objects.get(id=reader_id)
            except Reader.DoesNotExist:
                request.session.update(
                    {
                        'reader_id': self.READER_NOT_FOUND,
                        'reader_name': 'brak',
                        'reader_surname': 'brak'
                    }
                )
            else:
                request.session.update(
                    {
                        'reader_id': reader.id,
                        'reader_name': reader.name,
                        'reader_surname': reader.surname
                    }
                )
        return redirect(reverse('reader-profile'))


class BorrowBookView(View):
    def get(self, request):
        ctx = {
            'id_book_form': IdBookForm()
        }
        return render(request, 'librarian/borrow-book.html', context=ctx)

    def in_borrow(self, book):
        borrow = Borrowing.objects.filter(book=book)
        return bool(borrow)
    
    def post(self, request):
        form = IdBookForm(request.POST)
        request.session['book_in_catalog'] = True
        request.session['book_in_library'] = False
        if form.is_valid():
            book_id = form.cleaned_data['id']
            try:
                book = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                request.session['book_in_catalog'] = False
            else:
                if not self.in_borrow(book):
                    request.session['book_in_library'] = True
                    reader = Reader.objects.get(
                        pk=request.session['reader_id']
                    )
                    borrowing = Borrowing(reader=reader, book=book)
                    borrowing.save()
        return redirect(reverse('book-is-borrow'))


class BookIsBorrow(View):
    def get(self, request):
        return render(request, 'librarian/book-is-borrow.html')
    

class LoanExtension(View):
    pass
