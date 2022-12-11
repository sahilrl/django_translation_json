from django.test import TestCase
from booklist.forms import get_field_info


class BookTest(TestCase):
    @classmethod 
    def setUpTestData(self):
        from booklist.models import AbstractModel
        from django.db import models

        class TestModel(AbstractModel):
            field1 = models.CharField(max_length=500, blank=False, null=False)
            field2 = models.CharField(max_length=500, blank=False, null=False)

            def __str__(self):
                return self.field1
        self.model = TestModel

    def test_form_fields(self):
        fields = ['field1', 'field2', 'field1_ru', 'field1_es', 'field2_ru', 'field2_es']
        self.form = get_field_info(self.model)
        form_obj = self.form()
        self.assertTrue(set(list(form_obj.fields.keys())).issubset(fields))
        

    def test_admin_registration(self):
        from booklist.abstractAdmin import LocaleAdminSite
        from django.contrib import admin
        
        class TestAdminSite(LocaleAdminSite):
            form = get_field_info(self.model)
        try:
            admin.site.register(self.model, TestAdminSite)
        except Exception as ex:
            raise(ex)


        





