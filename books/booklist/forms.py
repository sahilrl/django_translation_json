from django.conf import settings
from django import forms
from .models import Books
from booklist.utils import build_localized_fieldname


class BooksForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        b = Books
        for i in b.get_field_info(self):
            for lang in settings.LANGUAGES:
                field_name = '%s_%s' % (i[0], lang[0])
                # TODO: set form field type acc. to original field in models?
                self.fields[field_name] = forms.CharField(required=False)
    

                
            





