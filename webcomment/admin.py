from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from webcomment.models import СommentMode


@admin.register(СommentMode)
class СommentModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'comment', 'date']
    list_display_links = ['id', 'comment', 'date']
    search_fields = ['comment']
