from .models import Book
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

# Create your views here.
