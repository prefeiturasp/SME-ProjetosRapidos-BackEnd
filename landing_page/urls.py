from .views import SectionViewSet

app_name = "landing_page"

routeList = (
    (r'section', SectionViewSet),
)
