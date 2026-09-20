from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BooksIndexView.as_view(), name="index"),
    path("book/<slug:slug>", views.BookDetailView.as_view(), name="book_detail"),
]
