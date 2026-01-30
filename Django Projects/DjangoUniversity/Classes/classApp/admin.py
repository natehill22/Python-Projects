from django.contrib import admin
from .models import UniversityClasses

#Registers the imported model to make it visible in the admin panel
admin.site.register(UniversityClasses)


