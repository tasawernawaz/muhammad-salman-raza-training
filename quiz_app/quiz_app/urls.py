from django.contrib import admin
from django.urls import include, path
# drf-spectacular
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# drf-yasg
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version="v1",
        description="This is the detailed view on all apis available in the quiz app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="salman.raza@arbisoft.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    path("quiz/", include("quiz.urls")),
    path(
        "yasg/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "yasg/swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("spectacular/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "spectacular/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "spectacular/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
