from django.urls import path
from .views import studentView, createStudent
urlpatterns = [
    path('view/', studentView),
    path('create/', createStudent),
]
