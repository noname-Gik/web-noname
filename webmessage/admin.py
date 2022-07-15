from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from webmessage.models import MessageMode, PhotoFileMode


@admin.register(MessageMode)
class MessageModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'textsend', ]
    list_display_links = ['id', 'textsend', ]
    search_fields = ['textsend', ]


@admin.register(PhotoFileMode)
class PhotoFileModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'file']
    list_display_links = ['id', 'file']
    search_fields = ['id']
