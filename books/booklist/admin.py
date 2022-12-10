from booklist.forms import get_field_info
from booklist.abstractAdmin import LocaleAdminSite
from django.contrib import admin
from booklist.models import Books, Library




class BookAdminSite(LocaleAdminSite):
    form = get_field_info(Books)
        

class LibraryAdminSite(LocaleAdminSite):
    form = get_field_info(Library)


admin.site.register(Books, BookAdminSite)
admin.site.register(Library, LibraryAdminSite)