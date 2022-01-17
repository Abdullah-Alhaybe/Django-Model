from django.contrib import admin

# Register your models here.
from .models import klanten , Question ,Questionnaire , Answer

admin.site.register(klanten)
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Answer)

