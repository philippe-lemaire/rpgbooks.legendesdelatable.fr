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


class BooksIndexView(ListView):
    context_object_name = "books"
    model = Book
    paginate_by = 10


def books_by_system_view(request, slug):
    system = System.objects.filter(slug=slug)[0]
    queryset = Book.objects.filter(system=system)
    template_name = "books/book_list.html"
    context = {"books": queryset, "filtered_by": f"System: {system}"}
    return render(request, template_name, context)


def books_by_tag_view(request, slug):
    tag = Tag.objects.filter(slug=slug)[0]
    slug = tag.slug
    queryset = Book.objects.filter(tags__slug=slug)
    template_name = "books/book_list.html"
    context = {"books": queryset, "filtered_by": f"Tag: {tag}"}
    return render(request, template_name, context)


class BookDetailView(DetailView):
    model = Book


class SystemsListView(ListView):
    model = System


class TagsListView(ListView):
    model = Tag
