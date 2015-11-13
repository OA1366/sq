from django.contrib import admin
from books.models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Age', 'Country')
    search_fields = ('Name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Publisher', 'PublishDate', 'Price')
#    list_fliter = ('PublishDate',)
#    date_hierarchy = 'PublishDate'
    ordering = ('PublishDate',)
#    fields = ('Title', 'Publisher', 'Price')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
