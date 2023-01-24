from django.contrib import admin
from general.models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    model = ContactMessage
    list_display = ('name', 'email', 'message', )


admin.site.register(ContactMessage, ContactMessageAdmin)
