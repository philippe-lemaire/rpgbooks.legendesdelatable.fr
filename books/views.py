from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

from .models import Book, System, Tag

# Create your views here.


def fix_choice_display(qs):
    for book in qs:
        book.display_book_type = book.get_book_type_display()


class BooksIndexView(ListView):
    context_object_name = "books"
    model = Book
    paginate_by = 10


def book_list_view(request):
    books = Book.objects.all()
    fix_choice_display(books)
    template_name = "books/book_list.html"
    context = {"books": books}
    return render(request, template_name, context)


def books_by_system_view(request, slug):
    system = System.objects.filter(slug=slug)[0]
    queryset = Book.objects.filter(system=system)
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {"books": queryset, "filtered_by": f"System: {system}"}
    return render(request, template_name, context)


def books_by_book_type_view(request, book_type):
    queryset = Book.objects.filter(book_type=book_type)
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {
        "books": queryset,
        "filtered_by": f"Book type: {queryset[0].get_book_type_display()}",
    }
    return render(request, template_name, context)


def books_by_tag_view(request, slug):
    tag = Tag.objects.filter(slug=slug)[0]
    slug = tag.slug
    queryset = Book.objects.filter(tags__slug=slug)
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {"books": queryset, "filtered_by": f"Tag: {tag}"}
    return render(request, template_name, context)


def book_detail_view(request, slug):
    book = Book.objects.get(slug=slug)
    book.display_book_type = book.get_book_type_display()
    template_name = "books/book_detail.html"
    context = {
        "book": book,
    }
    return render(request, template_name, context)


class SystemsListView(ListView):
    model = System


class TagsListView(ListView):
    model = Tag
