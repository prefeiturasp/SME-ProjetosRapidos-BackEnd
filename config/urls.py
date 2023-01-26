from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from general import urls as general_routes
from project_request import urls as project_request_routes
from landing_page import urls as landing_page_routes

admin.site.site_title = 'Projetos rápidos'
admin.site.site_header = 'Projetos rápidos'
admin.site.index_title = 'Projetos rápidos ADMIN'

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

routeLists = [
    general_routes.routeList,
    project_request_routes.routeList,
    landing_page_routes.routeList
]

for routeList in routeLists:
    for route in routeList:
        try:
            router.register(route[0], route[1], route[2])
        except:
            router.register(route[0], route[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
