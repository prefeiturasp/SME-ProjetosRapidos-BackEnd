from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from general.models import ContactMessage
from general.serializers import ContactMessageSerializer
from general.utils import send_email_new_contact_message


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            instance = ContactMessage.objects.get(pk=serializer.data['id'])
            send_email_new_contact_message(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
