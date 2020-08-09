from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book as B


# Adding a class
class Another(View):

    books = B.objects.all()
    output = ""

    for book in books:
      output += f"We have {book.title} books in DB with ID: {book.id}<br>"
      print(book.title)
      print(book.genre)
      print(book.kid_friendly)
      print(book.status)
      print(book.description)
      print(book.price)
      print(book.published)
      print(book.cover)

    def get(self, request):
        print(self.output)
        return HttpResponse(self.output)

    def hello(self, request):
        return HttpResponse("Hello from another view")


def first(request):
    return HttpResponse("First Message from Views")

def hello(request):
    return HttpResponse("Hello World!")