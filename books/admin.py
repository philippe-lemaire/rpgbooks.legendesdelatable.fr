from django.contrib import admin

# Register your models here.
from .models import Book, Tag, System


class BookAdmin(admin.ModelAdmin):
    search_fields = ["title", "system"]
    list_display = ["title", "system", "authors"]


admin.site.register(Book, BookAdmin)
admin.site.register(Tag)
admin.site.register(System)
