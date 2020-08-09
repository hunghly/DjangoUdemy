from django.shortcuts import render
from django.http import HttpResponse
from django.views import View



# Adding a class
class Another(View):

    def get(self, request):
        return HttpResponse("This is another function inside class")

    def hello(self, request):
        return HttpResponse("Hello from another view")


def first(request):
    return HttpResponse("First Message from Views")

def hello(request):
    return HttpResponse("Hello World!")