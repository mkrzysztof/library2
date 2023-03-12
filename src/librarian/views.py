from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.base import (TemplateView, )
from django.views.generic.edit import FormView

from .forms import IdReaderForm

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
    def get(self, request):
        return render(request, 'librarian/reader.html')

    def post(self, request):
        form = IdReaderForm(request.POST)
        if 'reader_id' in request.session:
            del request.session['reader_id']
        if form.is_valid():
            reader_id = form.cleaned_data['id']
            request.session['reader_id'] = reader_id
        return redirect(reverse('reader-profile'))


class BorrowBookView(TemplateView):
    template_name = 'librarian/borrow-book.html'


class LoanExtension(View):
    pass
