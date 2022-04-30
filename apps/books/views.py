from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from apps.books.models import Book
from apps.books.forms import BookForm

# List View
class BookList(ListView):
    model = Book

# Detail View
class BookView(DetailView):
    model = Book

# Create View
class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

# Update View
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

# Delete View
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')