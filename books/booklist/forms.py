from django.conf import settings
from django import forms
from booklist.utils import build_localized_fieldname, build_localized_verbose_name
import json
from collections import OrderedDict

def get_field_info(model_name):
    """
    This functions takes a model and populate the field_info_list with its fields.
    The ignore_fields list ignores "id" and "locale" for which we do not
    want to create localized fields. The function creates a Form with the localized fields
    and it returns the LocalForm.
    """
    fields = model_name._meta.get_fields()
    field_info_list = []
    # TODO: take ignore_fields from the model specified and append it here
    ignore_fields = ['id', 'locale']
    for i in fields:
        if i.name not in ignore_fields:
            field_info_list.append((i.name, i.get_internal_type()))


    class LocaleForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #  field_info_list  -> [('title', 'CharField'), ('author', 'CharField')]
            for field_name, field_type in field_info_list:
                for lang in settings.LANGUAGES:
                    if lang[0] not in settings.LANGUAGE_CODE:
                        field = build_localized_fieldname(field_name, lang[0])
                        label = build_localized_verbose_name(field_name, lang[0])
                        # TODO: set form field type acc. to original field in models?
                        self.fields[field] = forms.CharField(required=False, label=label)
            self.fields = OrderedDict(sorted(self.fields.items()))

        class Meta:
            model = model_name
            fields = []
            labels = {}
            for field_name in field_info_list:
                fields.append(field_name[0])
                labels[field_name[0]] = build_localized_verbose_name(field_name[0], settings.LANGUAGE_CODE)
            
        def save(self, commit):
            """ 
            The original fields defined in Model is saved by BaseModelForm save method
            Here, we are saving in Locale field the extra translation fields as JSON
            """
            stored_fields = {}
            for field in self.cleaned_data:
                # lang_code: title_ru -> [title, ru] or titile_en_us ->[title, us, en] or [title]
                lang_code = field.split("_")
                if len(lang_code) > 1:
                    if lang_code[1] in [lang[0] for lang in settings.LANGUAGES]:
                        if lang_code[1] not in stored_fields:
                            stored_fields[lang_code[1]] = []
                        stored_fields[lang_code[1]] += [{lang_code[0]: self.cleaned_data[field]}]
            # stored_fields => {'ru': [{'title': 'value'}, {'author': 'value'}], 'es': [{'title': 'value'}]}
            self.instance.locale = json.dumps(stored_fields)
            return super().save(commit=False)
              
    return LocaleForm


