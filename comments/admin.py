from django.contrib import admin
from .models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Comment, CommentAdmin)
