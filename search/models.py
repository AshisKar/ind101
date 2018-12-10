from django.db import models
from enum import Enum
from .constants import MINISTRY, OCCUPATION, TYPE, GENDER, CASTE, CATEGORY, AGE, INCOME_RANGE
from django.urls import reverse
from django.template.defaultfilters import slugify


class Ministry(models.Model):
    name_of_ministry = models.CharField(max_length=15, choices=MINISTRY)
    #scheme_name = models.CharField('Scheme',on_delete=models.SET_NULL, null=True)

class Job(models.Model):
    occupation = models.CharField(max_length=20, choices=OCCUPATION)


class Typ(models.Model):
    type_of_scheme = models.CharField(max_length=20, choices=TYPE)


class Category(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY)


class Caste(models.Model):
    caste = models.CharField(max_length=20, choices=CASTE)

class Scheme(models.Model):
    name = models.CharField(max_length=50)
    brief_info = models.TextField(max_length=1000)
    age = models.IntegerField(choices=AGE, help_text='enter age')
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    annual_income_range = models.CharField(max_length=15,choices=INCOME_RANGE,
                                           help_text='enter annual income', default='any')

    ministry = models.ForeignKey('Ministry', on_delete=models.SET_NULL, null=True, help_text='Select ministry')
    source_of_livelihood = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True, help_text='Select typ of job')
    caste = models.ForeignKey('Caste', on_delete=models.SET_NULL, null=True, help_text='Select typ of caste')
    typ = models.ForeignKey('Typ', on_delete=models.SET_NULL, null=True, help_text='Select type :Govt/Non-Govt')
    category = models.ManyToManyField('Category', help_text='Select category :Education/Health/Employment')
    slug = models.SlugField(slugify(name))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('scheme-detail-view', kwargs={"slug": self.slug})
