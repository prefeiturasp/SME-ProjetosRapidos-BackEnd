from django.contrib import admin
from project_request.models import ProjectRequest


class ProjectRequestAdmin(admin.ModelAdmin):
    model = ProjectRequest
    list_display = ('name', 'contact', 'register_datetime', )


admin.site.register(ProjectRequest, ProjectRequestAdmin)
