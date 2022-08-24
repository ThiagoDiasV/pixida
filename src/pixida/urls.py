from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from pixida.todo.urls import urlpatterns as todos_urls


schema_view = get_schema_view(
    openapi.Info(
        title='To-Do API',
        description='The To-Do API manages a To-Do list.',
        default_version='1.0.0',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_view = schema_view.with_ui("swagger", cache_timeout=0)


api_urls = [
    *todos_urls
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(api_urls)),
    path('docs/', swagger_view, name='docs')
]
