from django.contrib import admin
from . import models
# Register your models here.

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    search_fields = ['name']

admin.site.register(models.PersonalInfo)
admin.site.register(models.About)
admin.site.register(models.Projects)
admin.site.register(models.Skills)
