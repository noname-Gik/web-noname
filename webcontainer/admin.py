from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from webcontainer.models import OrganizationTableMode, RoleTableMode, UserTableMode, ConnectionTableMode


@admin.register(OrganizationTableMode)
class OrganizationTableModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(RoleTableMode)
class RoleTableModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(UserTableMode)
class UserTableModeAdmin(ImportExportModelAdmin):
    list_display = ['id', '__str__']
    list_display_links = ['id', '__str__']
    search_fields = ['name', '__str__']


@admin.register(ConnectionTableMode)
class ConnectionTableModeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'organizations', 'roles', 'users']
    list_display_links = ['id', 'organizations', 'roles', 'users']
    search_fields = ['organizations', 'roles', 'users']
