from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BooksIndexView.as_view(), name="index"),
    path("book/<slug:slug>", views.BookDetailView.as_view(), name="book_detail"),
    path("systems/", views.SystemsListView.as_view(), name="systems_list"),
    path("systems/<slug:slug>", views.books_by_system_view, name="books_by_system"),
    path("tags/", views.TagsListView.as_view(), name="tags_list"),
]
