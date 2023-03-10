from django.urls import path
from .views import (LibrarianView, BookReturnView, ReaderProfileView,
                    SearchView)

urlpatterns = [
    path('', LibrarianView.as_view(), name='index'),
    path('return-book', BookReturnView.as_view(), name='return-book'),
    path('user-profile', ReaderProfileView.as_view(), name='reader-profile'),
    path('catalog', SearchView.as_view(), name='catalog'),
]
