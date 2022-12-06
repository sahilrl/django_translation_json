from django.conf import settings
from django import forms
from .models import Books
from booklist.utils import build_localized_fieldname


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        b = Books
        for i, j in b.get_field_info(self):
            for lang in settings.LANGUAGES:
                field_name = build_localized_fieldname(i, lang[0])
                # TODO: set form field type acc. to original field in models?
                if lang[0] in settings.LANGUAGE_CODE:
                    print(lang[0], settings.LANGUAGE_CODE)
                    self.fields[field_name] = forms.CharField()
                else:
                    self.fields[field_name] = forms.CharField()
    
    def save(self):
        author_ru = self.cleaned_data.get('author_ru', None)
        return super().save(commit="commit")

                
            





