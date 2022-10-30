from django.contrib import admin

# Register your models here.
from .models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'isbn', 'description')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'bio')

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'book')

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'stars_given', 'book')



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)

