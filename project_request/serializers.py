from rest_framework import serializers
from project_request.models import ProjectRequest


class ProjectRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRequest
        fields = '__all__'
