import logging
logging.basicConfig(level=logging.INFO)

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import (TemplateView, )
from django.views.generic.edit import FormView

from .forms import (IdReaderForm, IdBookForm)
from .models import (Reader, Book, Borrowing)

# Create your views here.

class LibrarianView(FormView):
    template_name = 'librarian/index.html'
    form_class = IdReaderForm
    

class SearchView(View):
    def get(self, request):
        return render(request, 'librarian/search.html')


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


def in_borrow(book):
    borrow = Borrowing.objects.filter(book=book)
    return bool(borrow)


class BorrowBookView(View):
    def get(self, request):
        ctx = {
            'id_book_form': IdBookForm()
        }
        return render(request, 'librarian/borrow-book.html', context=ctx)

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
                if not in_borrow(book):
                    request.session['book_in_library'] = True
                    reader = Reader.objects.get(
                        pk=request.session['reader_id']
                    )
                    borrowing = Borrowing(reader=reader, book=book)
                    borrowing.save()
        return redirect(reverse('book-is-borrow'))


class BookIsBorrowView(TemplateView):
    template_name = 'librarian/book-is-borrow.html'
    

class ReturnBookView(View):
    def get(self, request):
        ctx = {
            'id_book_form': IdBookForm()
        }
        return render(request, 'librarian/return_book.html', context=ctx)

    def post(self, request):
        form = IdBookForm(request.POST)
        request.session['book_in_catalog'] = True
        request.session['book_is_borrow'] = False
        if form.is_valid():
            book_id = form.cleaned_data['id']
            try:
                book = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                request.session['book_in_catalog'] = False
            else:
                if in_borrow(book):
                    request.session['book_is_borrow'] = True
                    borrow = Borrowing.objects.get(book=book)
                    borrow.delete()
        return redirect(reverse('book-is-return'))


class BookIsReturnView(TemplateView):
    template_name = 'librarian/book-is-return.html'
        

class LoanExtension(View):
    pass
