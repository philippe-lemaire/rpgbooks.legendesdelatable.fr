from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    # path("", views.BooksIndexView.as_view(), name="index"),
    path("", views.book_list_view, name="index"),
    path("book/<slug:slug>", views.book_detail_view, name="book_detail"),
    path("systems/", views.SystemsListView.as_view(), name="systems_list"),
    path("systems/<slug:slug>", views.books_by_system_view, name="books_by_system"),
    path("tags/", views.TagsListView.as_view(), name="tags_list"),
    path("tags/<slug:slug>", views.books_by_tag_view, name="books_by_tag"),
    path(
        "book-type/<str:book_type>",
        views.books_by_book_type_view,
        name="books_by_book_type",
    ),
]
