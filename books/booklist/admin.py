from django.contrib import admin
from booklist.models import Books
from booklist.forms import BooksForm
from django.template.response import TemplateResponse
from django.urls import path


class BooksAdminSite(admin.AdminSite):
    index_template = 'admin/admin.html'
    app_index_template = 'admin/admin_app.html'
    
   

admin_site = BooksAdminSite(name='Myadmin')
admin_site.register(Books)
