from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    author = models.CharField(max_length=500, null=True, blank=True)
    genre = models.CharField(max_length=500, null=True, blank=True)
    locale = models.JSONField()

    def __str__(self):
        return self.title

   
class Library(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    location = models.CharField(max_length=500, null=True, blank=True)
    locale = models.JSONField()
    
    def __str__(self):
        return self.name



    






