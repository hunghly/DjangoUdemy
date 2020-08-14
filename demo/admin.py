from django.contrib import admin
from .models import Book, BookNumber

# Register your models here.
# admin.site.register(Book)

# You can decide which fields you want to display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'description']
    list_filter = ['published', 'title']
    search_fields = ['title', 'description']

@admin.register(BookNumber)
class BookNumberAdmin(admin.ModelAdmin):
    list_display = ['isbn_10', 'isbn_13']
    list_filter = ['isbn_10', 'isbn_13']
    search_fields = ['isbn_10', 'isbn_13']