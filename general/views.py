from rest_framework import viewsets
from general.models import ContactMessage
from general.serializers import ContactMessageSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post']
