from django.contrib import admin

from .models import Scheme, Ministry, Job, Typ, Category, Caste

admin.site.register(Scheme)
admin.site.register(Ministry)
admin.site.register(Job)
admin.site.register(Typ)
admin.site.register(Category)
admin.site.register(Caste)

