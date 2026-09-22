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


def book_list_view(request):
    books = Book.objects.all().order_by("system")
    fix_choice_display(books)
    template_name = "books/book_list.html"
    context = {
        "books": books,
        "book_types": Book.BOOK_TYPE_CHOICES,
    }
    return render(request, template_name, context)


def books_by_want_to_run(request):
    queryset = Book.objects.filter(want_to_run=True).order_by("system")
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {
        "books": queryset,
        "filtered_by": "Want to run",
        "book_types": Book.BOOK_TYPE_CHOICES,
    }
    return render(request, template_name, context)


def books_by_system_view(request, slug):
    system = System.objects.filter(slug=slug)[0]
    queryset = Book.objects.filter(system=system).order_by("system")
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {
        "books": queryset,
        "filtered_by": f"System: {system}",
        "book_types": Book.BOOK_TYPE_CHOICES,
    }
    return render(request, template_name, context)


def books_by_book_type_view(request, book_type):
    queryset = Book.objects.filter(book_type=book_type).order_by("system")
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {
        "books": queryset,
        "book_types": Book.BOOK_TYPE_CHOICES,
    }
    if queryset:
        context["filtered_by"] = (f"Book type: {queryset[0].get_book_type_display()}",)
    return render(request, template_name, context)


def books_by_tag_view(request, slug):
    tag = Tag.objects.filter(slug=slug)[0]
    slug = tag.slug
    queryset = Book.objects.filter(tags__slug=slug).order_by("system")
    fix_choice_display(queryset)
    template_name = "books/book_list.html"
    context = {
        "books": queryset,
        "filtered_by": f"Tag: {tag}",
        "book_types": Book.BOOK_TYPE_CHOICES,
    }
    return render(request, template_name, context)


def book_detail_view(request, slug):
    book = Book.objects.get(slug=slug)
    book.display_book_type = book.get_book_type_display()
    template_name = "books/book_detail.html"
    context = {
        "book": book,
        "book_types": Book.BOOK_TYPE_CHOICES,
    }
    return render(request, template_name, context)


class SystemsListView(ListView):
    model = System

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_types"] = Book.BOOK_TYPE_CHOICES
        return context


class TagsListView(ListView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_types"] = Book.BOOK_TYPE_CHOICES
        return context
