from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=500)
    locale = models.JSONField()

    def __str__(self):
        return self.title

    def get_field_info(self):
        """ returns a field_info_list which contains
            tuples with field name and type
        """
        fields = Books._meta.get_fields()
        field_info_list = []
        ignore_fields = ['id', 'locale']
        for i in fields:
            if i.name not in ignore_fields:
                field_info_list.append((i.name, i.get_internal_type()))
        return field_info_list

    
    


