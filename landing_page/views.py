from rest_framework import viewsets
from landing_page.models import Section
from landing_page.serializers import SectionSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    http_method_names = ['get']
