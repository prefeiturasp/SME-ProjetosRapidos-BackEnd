from rest_framework import serializers
from landing_page.models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
