from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.db import  router, transaction

csrf_protect_m = method_decorator(csrf_protect)

class LocaleAdminSite(admin.ModelAdmin):
    """ 
        This is the baseclass that you can sub-class in the admin.py,
        and in the subclass set the value for form like
        form = get_field_info(model_name). you can import get_field_info from forms.py
        after that you need to register your subclass like
        admin.site.register(model_name, SubclassAdminSite)
    """
    index_template = 'admin/admin.html'
    app_index_template = 'admin/admin_app.html'
    form = ""
    
    # here we provided our custom form and also we have removed the default form from the template
    def change_view(self, request, object_id, form_url="", extra_context=None):
        if request.method == 'POST':
            form = self.form(request.POST)
        context = {}
        form = self.form()
        context['form'] = form
        return self.changeform_view(request, object_id, form_url, extra_context=context)
    
    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if request.method == 'POST':
            form = self.form(request.POST)
            print(form)
        form = self.form()
        context = {}
        context['form'] = form
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._changeform_view(request, object_id, form_url, extra_context=context)


