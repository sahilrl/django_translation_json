from django.test import TestCase


class BookTest(TestCase):
    @classmethod 
    def setUpTestData(self):
        from booklist.models import AbstractModel
        from booklist.forms import get_field_info
        from django.db import models

        class TestModel(AbstractModel):
            field1 = models.CharField(max_length=500, blank=False, null=False)
            field2 = models.CharField(max_length=500, blank=False, null=False)

            def __str__(self):
                return self.field1
        self.model = TestModel
        self.form = get_field_info(self.model)

    def test_form_fields(self):
        fields = ['field1', 'field2', 'field1_ru', 'field1_es', 'field2_ru', 'field2_es']
        form = self.form()
        self.assertTrue(set(list(form.fields.keys())).issubset(fields))
        

    def test_admin_registration(self):
        from booklist.abstractAdmin import LocaleAdminSite
        from django.contrib import admin
        
        class TestAdminSite(LocaleAdminSite):
            form = self.form()
        try:
            admin.site.register(self.model, TestAdminSite)
        except Exception as ex:
            raise(ex)

    def test_form_save(self):
        pass



        





