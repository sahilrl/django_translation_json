from django.contrib import admin
from booklist.forms import BooksForm


class BooksAdmin(admin.ModelAdmin):
    form = BooksForm
    add_fieldsets = (
        (None, {
            'fields': ('*'),
        }),
    )





