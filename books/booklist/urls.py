from django.urls import path
from booklist import views
from booklist.admin import admin_site
from booklist.forms import BooksForm

form = BooksForm()

urlpatterns = [
    path('', views.bookform, name="bookform"),
    path('myadmin/', admin_site.urls, {'extra_context': {'form': form}}),
]
