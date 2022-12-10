from booklist.forms import get_field_info
from booklist.abstractAdmin import LocaleAdminSite
from django.contrib import admin
from booklist.models import Books, Library

# here you can subclass LocalAdminSite.
# 
# class SubClassAdmin(LocalAdminSite):
#   form = get_field_info(model_name)
#
# and then register your subclass
# admin.site.register(model_name, SubClassAdmin)


class BookAdminSite(LocaleAdminSite):
    form = get_field_info(Books)
        

class LibraryAdminSite(LocaleAdminSite):
    form = get_field_info(Library)


admin.site.register(Books, BookAdminSite)
admin.site.register(Library, LibraryAdminSite)