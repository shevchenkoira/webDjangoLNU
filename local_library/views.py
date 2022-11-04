from django.http import Http404
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_genres': num_genres
    }

    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'local_library/book_list.html'
    paginate_by = 5


def book_detail_view(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    context = {
        'book': book,
    }

    return render(request, 'local_library/book_detail.html', context)
