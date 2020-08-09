from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book as B


# Adding a class
class Another(View):

    books = B.objects.all()

    output = f

    def get(self, request):
        print(self.books)
        print(self.books[0])
        return HttpResponse("This is another function inside class")

    def hello(self, request):
        return HttpResponse("Hello from another view")


def first(request):
    return HttpResponse("First Message from Views")

def hello(request):
    return HttpResponse("Hello World!")