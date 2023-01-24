from .views import ContactMessageViewSet

app_name = "contact_message"

routeList = (
    (r'contact_message', ContactMessageViewSet),
)
