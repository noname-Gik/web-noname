from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from webmain.models import ButtonMode, PhotoFile


@admin.register(ButtonMode)
class ButtonModeAdmin(ImportExportModelAdmin):
    list_display = ['id', '__str__', 'link']
    list_display_links = ['id', '__str__']


@admin.register(PhotoFile)
class PhotoFileAdmin(ImportExportModelAdmin):
    list_display = ['id', 'file', ]
    list_display_links = ['id', 'file', ]
    search_fields = ['id', ]
