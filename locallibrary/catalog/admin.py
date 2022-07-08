from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.

# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(Author)
# admin.site.register(BookInstance)


class BookInline(admin.TabularInline):
    model = Book


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre',)

    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ('get_books', 'status', 'due_back', 'id',)
    list_filter = ('status', 'due_back',)

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Avalability', {'fields': ('status', 'due_back')}),
    )


admin.site.register(Author, AuthorAdmin)
