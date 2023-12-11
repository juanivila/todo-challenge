from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("notes.urls")),
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
