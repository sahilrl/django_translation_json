from django.contrib import admin
from booklist.models import Books
from booklist.forms import BooksForm
from django.template.response import TemplateResponse
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.db import  router, transaction

csrf_protect_m = method_decorator(csrf_protect)

class BooksAdminSite(admin.ModelAdmin):
    index_template = 'admin/admin.html'
    app_index_template = 'admin/admin_app.html'
    form = BooksForm

    def change_view(self, request, object_id, form_url="", extra_context=None):
        if request.method == 'POST':
            form = BooksForm(request.POST)
        context = {}
        form = BooksForm()
        context['form'] = form
        return self.changeform_view(request, object_id, form_url, extra_context=context)
    
    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if request.method == 'POST':
            form = BooksForm(request.POST)
            print(form)
        form = BooksForm()
        context = {}
        context['form'] = form
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._changeform_view(request, object_id, form_url, extra_context=context)


admin.site.register(Books, BooksAdminSite)



