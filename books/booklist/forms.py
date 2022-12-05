from django.conf import settings
from django import forms
from .models import Books
from booklist.utils import build_localized_fieldname


class BooksForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        b = Books
        for i, j in b.get_field_info(self):
            for lang in settings.LANGUAGES:
                field_name = build_localized_fieldname(i, lang[1])
                # TODO: set form field type acc. to original field in models?
                self.fields[field_name] = forms.CharField(required=False)
    

                
            





