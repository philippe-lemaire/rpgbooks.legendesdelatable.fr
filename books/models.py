from django.db import models
from tinymce.models import HTMLField


class System(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    cover = models.ImageField()
    # book_type choices Core Rule Book, Splat book, Setting book, Campaign Book, Module
    blurb = HTMLField(blank=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    want_to_run = models.BooleanField(default=False)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"Book: {self.title.title()}"
