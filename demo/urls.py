
from django.urls import path
from demo import views

urlpatterns = [
    path('', views.first),
    path('hello', views.hello)
]
