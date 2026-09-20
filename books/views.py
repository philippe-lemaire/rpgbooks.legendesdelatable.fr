from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from django.conf import settings

from .models import Book

# Create your views here.


class BooksIndexView(ListView):
    context_object_name = "books"
    model = Book
    paginate_by = 10


# template_name = "books/books_list.html"


class BookDetailView(DetailView):
    model = Book
