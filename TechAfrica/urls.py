from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TechAfrica API",
        default_version='v1',
        description="TechAfrica platform API documentation",
        terms_of_service="https://www.techafrica.com/terms/",
        contact=openapi.Contact(email="support@techafrica.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API routes
    path('api/accounts/', include('accounts.urls')),
    path('api/issues/', include('issues.urls')),
    path('api/solutions/', include('solutions.urls')),

    # Swagger UI as homepage
    path(
        '',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='swagger-home',
    ),

    # OpenAPI JSON/YAML (REQUIRED)
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),

    # ReDoc
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]

# Media files (image uploads)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
