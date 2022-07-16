from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from webmessage.models import FileMessageMode


@admin.register(FileMessageMode)
class FileMessageModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'textsend', 'docfile' ]
    list_display_links = ['id', 'textsend', 'docfile' ]
    search_fields = ['textsend', ]

