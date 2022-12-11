from django.db import models


class AbstractModel(models.Model):
    locale = models.JSONField()
    
    class Meta:
        abstract = True


class Books(AbstractModel):
    title = models.CharField(max_length=500, blank=False, null=False)
    author = models.CharField(max_length=500, null=True, blank=True)
    genre = models.CharField(max_length=500, null=True, blank=True)
   
    def __str__(self):
        return self.title

   
class Library(AbstractModel):
    name = models.CharField(max_length=500, blank=False, null=False)
    location = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name



    






