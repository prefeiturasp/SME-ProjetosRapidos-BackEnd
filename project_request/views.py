from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from project_request.models import ProjectRequest
from project_request.serializers import ProjectRequestSerializer
from project_request.utils import send_email_new_request_message


class ProjectRequestViewSet(viewsets.ModelViewSet):
    queryset = ProjectRequest.objects.all()
    serializer_class = ProjectRequestSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # send_email_new_request_message()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
