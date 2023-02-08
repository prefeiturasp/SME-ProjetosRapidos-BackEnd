from django.contrib import admin
from project_request.models import ProjectRequest
from import_export.admin import ImportExportModelAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter


class ProjectRequestAdmin(ImportExportModelAdmin):
    model = ProjectRequest
    list_display = ('coordenadoria', 'name', 'approx_release_date',)
    list_filter = (
        ('coordenadoria', DropdownFilter),
        ('register_datetime', DateRangeFilter),
        ('approx_release_date', DateRangeFilter),
    )


admin.site.register(ProjectRequest, ProjectRequestAdmin)
