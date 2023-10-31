from django.contrib import admin
from . import models

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created',)

admin.site.register(models.Note, NoteAdmin)