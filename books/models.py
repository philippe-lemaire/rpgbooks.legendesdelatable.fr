from django.db import models
from tinymce.models import HTMLField
from file_validator.models import DjangoFileValidator


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
    slug = models.SlugField()
    authors = models.CharField(max_length=300, blank=True)
    cover = models.ImageField(
        blank=True,
        upload_to="covers/",
        validators=[
            DjangoFileValidator(
                libraries=[
                    "python_magic",
                    "filetype",
                ],  # => validation operations will be performed with python-magic and filetype libraries
                acceptable_mimes=[
                    "image/png",
                    "image/jpeg",
                    "image/jpg",
                    "image/webp",
                ],  # => The mimes you want the file to be checked based on.
                acceptable_types=["image"],
                max_upload_file_size=5242880,
            )
        ],
    )  # => 5 MB)
    BOOK_TYPE_CHOICES = (
        ("CRB", "Core Rule Book"),
        ("STS", "Starter Set"),
        ("SPB", "Splat Book"),
        ("SB", "Setting Book"),
        ("CB", "Campaign Book"),
        ("MOD", "Module"),
        ("BES", "Bestiary"),
    )
    book_type = models.CharField(
        max_length=3, choices=BOOK_TYPE_CHOICES, default=BOOK_TYPE_CHOICES[0][0]
    )
    # book_type choices Core Rule Book, Splat book, Setting book, Campaign Book, Module
    blurb = HTMLField(blank=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    want_to_run = models.BooleanField(default=False)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"Book: {self.title.title()}"
