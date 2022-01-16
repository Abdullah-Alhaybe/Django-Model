from django.contrib import admin

# Register your models here.

from .models import project , progress , intern

admin.site.register(project)
admin.site.register(progress)
admin.site.register(intern)