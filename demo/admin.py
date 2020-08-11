from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)

# You can decide which fields you want to display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'description']
    list_filter = ['published', 'title']
    search_fields = ['title', 'description']