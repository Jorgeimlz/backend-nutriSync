# NutriSync/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configura la vista del esquema para Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de NutriSync",
        default_version='v1',
        description="Documentación de la API para el proyecto NutriSync.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@nutrisync.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/ingredientes/', include('ingredientes.urls')),
    path('api/categorias/', include('categorias.urls')),
    path('api/recetas/', include('recetas.urls')),
    path('api/dietas/', include('dieta.urls')),  # Asegúrate de que esta línea esté presente
    path('api/planes-alimenticios/', include('planes_alimenticios.urls')),  # Asegúrate de que esta línea esté presente
]
