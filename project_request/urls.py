from .views import ProjectRequestViewSet

app_name = "project_request"

routeList = (
    (r'project_request', ProjectRequestViewSet),
)
