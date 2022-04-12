from atexit import register
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Series


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'series')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_author', 'owner', 'current_holder')
    list_filter = ('owner', 'current_holder')

    @admin.display(description='Title')
    def get_title(self, obj):
        return obj.book.title

    @admin.display(description='Author')
    def get_author(self, obj):
        return obj.book.author

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass