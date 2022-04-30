from django.urls import path

from apps.books.views import (
    BookList,
    BookCreate,
    BookView,
    BookUpdate,
    BookDelete,
)

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('new', BookCreate.as_view(), name='book_new'),
    path('view/id', BookView.as_view(), name='book_view'),
    path('edit/id>', BookUpdate.as_view(), name='book_edit'),
    path('delete/id', BookDelete.as_view(), name='book_delete'),
]