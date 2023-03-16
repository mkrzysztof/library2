import logging

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import (TemplateView, )
from django.views.generic.edit import FormView

from .forms import (IdReaderForm, IdBookForm)
from .models import Reader

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
        ctx = {
            'reader_id': request.session['reader_id'],
            'reader_name': request.session['reader_name'],
            'reader_surname': request.session['reader_surname']
        }
        return render(request, 'librarian/reader.html', context=ctx)

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

    def post(self, request):
        form = IdBookForm(request.POST)
        if form.is_valid():
            self.test = form.cleaned_data['id']
            print(self.test)
        return redirect(reverse('borrow-book'))


class LoanExtension(View):
    pass
