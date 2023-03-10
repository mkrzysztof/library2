from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

class LibrarianView(TemplateView):
    template_name = 'librarian/index.html'
        


class SearchView(View):
    def get(self, request):
        return render(request, 'librarian/search.html')


class BookReturnView(View):
    def get(self, request):
        return render(request, 'librarian/return_book.html')


class ReaderProfileView(View):
    def get(self, request):
        return render(request, 'librarian/reader.html')


class LendBook(View):
    pass


class LoanExtension(View):
    pass
