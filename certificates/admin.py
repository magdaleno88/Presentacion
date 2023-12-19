from django.contrib import admin
from .models import *
# Register your models here.

class CategoyuAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)



class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)



admin.site.register(Category, CategoyuAdmin)
admin.site.register(Certificate)
admin.site.register(Company, CompanyAdmin)