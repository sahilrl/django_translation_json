from django.conf import settings
from django import forms
from .models import Books
from booklist.utils import build_localized_fieldname, build_localized_verbose_name
from django.conf import settings
import json
    
b = Books()


class BooksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, j in b.get_field_info():
            for lang in settings.LANGUAGES:
                # do not create field for language in LANGUAGE_CODE
                if lang[0] not in settings.LANGUAGE_CODE:
                    field_name = build_localized_fieldname(i, lang[0])
                    # TODO: set form field type acc. to original field in models?
                    if lang[0] not in settings.LANGUAGE_CODE:
                        self.fields[field_name] = forms.CharField()
                    else:
                        self.fields[field_name] = forms.CharField()
                  
    class Meta:
        model = Books
        fields = []
        labels = { }
        # Appending all the fields (for rendering) and building localized verbose for labels
        # we removed the original form rendered by default in the change_form.html template.
        # Because the model fields were being duplicated in our custom form and default one.
        for i in b.get_field_info():
            fields.append(i[0])
            labels[i[0]] = build_localized_verbose_name(i[0], settings.LANGUAGE_CODE)
           
    def save(self, commit):
        """ The original fields defined in Model is saved by BaseModelForm save method
        Here, we are saving the extra translation fields as JSON"""
        temp = {}
        for field in self.cleaned_data:
            # lang_code is spliting out the language code from the field name. 
            # example: title_ru -> [title, ru]
            lang_code = field.split("_")
            # accessing the language code as last index after spilting
            if lang_code[-1] in [lang[0] for lang in settings.LANGUAGES]:
                if lang_code[-1] not in temp:
                    temp[lang_code[-1]] = []
                    # lang_code[0] gives field name as "title" rather than "title_ru"
                    # example ->{'ru': [{'title': 'value'}, {'author': 'value'}], 'es': [{'title': 'value'}]}
                temp[lang_code[-1]] += [{lang_code[0]: self.cleaned_data[field]}]
                self.instance.locale = json.dumps(temp)
        return super().save(commit=False)
            





