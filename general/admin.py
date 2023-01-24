from django.contrib import admin
from general.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    model = ContactMessage
    list_display = ('name', 'email', 'message', 'register_datetime', )


admin.site.register(ContactMessage, ContactMessageAdmin)
