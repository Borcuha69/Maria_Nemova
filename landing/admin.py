from django.contrib import admin
from .models import *


class Section2Admin(admin.ModelAdmin):
    list_display = ['name', 'image']

    class Meta:
        model = Section2


admin.site.register(Section2, Section2Admin)
