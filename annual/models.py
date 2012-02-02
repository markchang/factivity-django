from django.db import models

# Create your models here.
class Category(models.Model):
    long_description = models.CharField(max_length=255)
    short_description = models.CharField(max_length=80)
    def __unicode__(self):
        return self.short_description

class Activity(models.Model):
    username = models.CharField(max_length=80)
    description = models.CharField(max_length=512)
    category = models.ForeignKey(Category)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.description
