from django import forms

from apps.books.models import Book


class BookForm(forms.ModelForm):

    # The solution originally retrieved from
    #
    # https://stackoverflow.com/questions/33452278/how-to-add-bootstrap-class-to-django-createview-form-fields-in-the-template
    #
    # Thanks to César

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control input-lg'
        }
        self.fields['author'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['publisher'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Book
        fields = ('title', 'author',)