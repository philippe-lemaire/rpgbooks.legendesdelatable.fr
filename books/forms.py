from django.forms import ModelForm
from books.models import Book
from tinymce.widgets import TinyMCE


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = []
        widgets = {"blurb": TinyMCE(attrs={"cols": 80, "rows": 30})}
