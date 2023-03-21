from django.urls import path
from .views import (LibrarianView, ReaderProfileView,
                    SearchView, BorrowBookView, BookIsBorrowView,
                    ReturnBookView, BookIsReturnView)

urlpatterns = [
    path('', LibrarianView.as_view(), name='index'),
    path('reader-profile', ReaderProfileView.as_view(), name='reader-profile'),
    path('catalog', SearchView.as_view(), name='catalog'),
    path('borrow-book', BorrowBookView.as_view(), name='borrow-book'),
    path('book-is-borrow', BookIsBorrowView.as_view(), name='book-is-borrow'),
    path('return-book', ReturnBookView.as_view(), name='return-book'),
    path('book-is-return', BookIsReturnView.as_view(), name='book-is-return'),
]
