from django.conf import settings
from django import forms
from booklist.utils import build_localized_fieldname, build_localized_verbose_name
import json

def get_field_info(model_name):
    """
    This functions takes a model and populate the field_info_list with its fields.
    The ignore_fields ignores fields like "id" and "locale" (Json Field) for which we do not
    want to create localized fields.
    The function creates a Form with the localized fields and it returns the LocalForm
    """
    # here we are populating the array "field_info_list"
    # with the fields of the specified model.
    fields = model_name._meta.get_fields()
    field_info_list = []
    # array for ignoring fields like id and locale
    # TODO: take ignore_fields from the model specified and 
    # append it here
    ignore_fields = ['id', 'locale']
    for i in fields:
        if i.name not in ignore_fields:
            field_info_list.append((i.name, i.get_internal_type()))

    class LocaleForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # the array field_info_list contains a tuple with fieldname and type
            # example -> ('title', 'CharField')
            for field_name, field_type in field_info_list:
                for lang in settings.LANGUAGES:
                    # do not create field for language in LANGUAGE_CODE
                    if lang[0] not in settings.LANGUAGE_CODE:
                        field_name = build_localized_fieldname(field_name, lang[0])
                        # TODO: set form field type acc. to original field in models? using field_type
                        self.fields[field_name] = forms.CharField(required=False)


        class Meta:
            model = model_name
            fields = []
            labels = {}
            # Appending all the fields (for rendering) and building localized verbose for labels.
            # The original form template variable has been removed which was rendered by default
            # in the change_form.html template. As the model fields were being duplicated 
            # because of our custom form and default one.
            for field_name in field_info_list:
                fields.append(field_name[0])
                labels[field_name[0]] = build_localized_verbose_name(field_name[0], settings.LANGUAGE_CODE)
            
        def save(self, commit):
            """ The original fields defined in Model is saved by BaseModelForm save method
            Here, we are saving the extra translation fields as JSON"""
            stored_fields = {}
            for field in self.cleaned_data:
                # lang_code is spliting out the language code from the field name. 
                # example: title_ru -> [title, ru] or titile_en_us ->[title, us, en] or just [title]
                lang_code = field.split("_")
                # if we have only one field like ["title"] with length 1 then we just ignore it, 
                # if we have array with length more than 1 like the example below
                # -> ["title", "en"] or ["title", "en", "us"], we take the index [1]
                # and append this as key in the stored_fields dictionary.
                if len(lang_code) > 1:
                    # before appending the key we also first check if the key 
                    # exists in the LANGUAGES array defined in the settings file.
                    if lang_code[1] in [lang[0] for lang in settings.LANGUAGES]:
                        if lang_code[1] not in stored_fields:
                            stored_fields[lang_code[1]] = []
                            # After spillting for example, "title_ru", 
                            # the lang_code[0] index gives us field name like "title"
                            # example ->{'ru': [{'title': 'value'}, {'author': 'value'}], 'es': [{'title': 'value'}]}
                        stored_fields[lang_code[-1]] += [{lang_code[0]: self.cleaned_data[field]}]
            self.instance.locale = json.dumps(stored_fields)
            return super().save(commit=False)
              
    return LocaleForm


