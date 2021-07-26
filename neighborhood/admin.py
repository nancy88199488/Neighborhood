from django.contrib import admin
from .models import Business,Neighborhood,Profile,Posts

# Register your models here.

admin.site.register(Business)
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Posts)