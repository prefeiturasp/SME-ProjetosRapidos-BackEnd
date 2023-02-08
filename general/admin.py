from django.contrib import admin
from general.models import ContactMessage
from import_export.admin import ImportExportModelAdmin


class ContactMessageAdmin(ImportExportModelAdmin):
    model = ContactMessage
    list_display = ('register_datetime', 'name', 'coordenadoria',)


admin.site.register(ContactMessage, ContactMessageAdmin)
