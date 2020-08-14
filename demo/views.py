from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book as B
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import BookSerializer


# Adding a class
class Another(View):

    # objects.all() gets all the objects using QuerySet
    # books = B.objects.all()
    # objects.filter() gets all the objects based on the filtered content, can use excludes as well
    # filtered_books = B.objects.filter(is_book_published=True)
    # objects.get() returns just one object
    # book = B.objects.get(id=2)
    output = ""
    # loops through each book and do some printing
    # for book in filtered_books:
    #     output += f"We have {book.title} books in DB with ID: {book.id}<br>"
    #     print(book.title)
    #     print(book.genre)
    #     print(book.kid_friendly)
    #     print(book.status)
    #     print(book.description)
    #     print(book.price)
    #     print(book.published)
    #     print(book.cover)



    def get(self, request):
        print(self.output)
        return HttpResponse(self.output)

    def hello(self, request):
        return HttpResponse("Hello from another view")


def first(request):
    return render(request, 'first_temp.html', {
        'data': 'this is some data from views',
        'joke': 'knock knock',
        'book': B.objects.get(id=2).title,
        'books': B.objects.all()
    })


def hello(request):
    return HttpResponse("Hello World!")

class BookViewSet(viewsets.ModelViewSet):
    # will create a variable with the serializer that we want to use
    serializer_class = BookSerializer
    # assigns the queryset that will be used for the viewset
    queryset = B.objects.all()
    authentication_classes = (TokenAuthentication,)
    # you can control the resources that require authentication with permission classes
    # permission_classes = (IsAuthenticated,)
