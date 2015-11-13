# -*- encoding: utf-8 -*-
from django.db import models
# Create your models here.
#class Publisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length=60)
#    state_province = models.CharField(max_length=30)
#    country = models.CharField(max_length=50)
#    website = models.URLField()
#    def __unicode__(self):
#        return self.name

class Author(models.Model):
    Name = models.CharField(max_length=60)
    Age = models.IntegerField()
    Country = models.CharField(max_length=60)
    def __unicode__(self):
        return u'%s %s %s' % (self.Name, self.Age, self.Country)

class Book(models.Model):
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=40)
    PublishDate = models.DateField(blank=True, null=True)
    Price = models.CharField(max_length=60)
    def __unicode__(self):
        return u'%s %s %s %s' % (self.Title, self.Publisher, self.PublishDate, self.Price)
