from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.books.models import Book
from apps.books.api.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def filter_book(self, archived):
        book_list = Book.objects.filter(archived=archived)
        serializer = self.get_serializer(book_list, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def archived(self, request):
        return self.filter_book(archived=True)

    @action(detail=False)
    def unarchived(self, request):
        return self.filter_book(archived=False)