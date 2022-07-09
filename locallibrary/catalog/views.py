
from django.views import generic
from django.shortcuts import render
from.models import Author, Book, BookInstance, Genre
# Create your views here.


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

    def get_context_data(self, **kwargs):
        author_book = Book.objects.all()
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['author_book'] = author_book
        return context


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # your own name for the list as a template variable

    # context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='war')[
    #     :5]  # Get 5 books containing the title war
    # # Specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_queryset(self):
    #     # Get 5 books containing the title war
    #     return Book.objects.filter(title__icontains='b')[:5]

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['book'] = Book.objects.all()
        return context


def index(request):
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genre = Genre.objects.count()

    book_title = Book.title

    genre_of_book = Genre.objects.all()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'book_title': book_title,
        'genre_of_book': genre_of_book,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
