
from django.urls import path, include
from . import views
from .views import Another, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first', views.first),
    path('another', Another.as_view()),
    # path('anotherhello', Another.),
    path('hello', views.hello)
]
