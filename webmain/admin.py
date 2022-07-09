from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from webmain.models import ButtonMode, PhotoFile, AdviceMode, TicketMode


@admin.register(ButtonMode)
class ButtonModeAdmin(ImportExportModelAdmin):
    list_display = ['id', '__str__', 'link']
    list_display_links = ['id', '__str__']


@admin.register(AdviceMode)
class AdviceModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name', ]


@admin.register(TicketMode)
class TicketModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'navzone']
    list_display_links = ['id', 'name', 'navzone']
    search_fields = ['name', 'navzone']


@admin.register(PhotoFile)
class PhotoFileAdmin(ImportExportModelAdmin):
    list_display = ['id', 'file', ]
    list_display_links = ['id', 'file', ]
    search_fields = ['id', ]
