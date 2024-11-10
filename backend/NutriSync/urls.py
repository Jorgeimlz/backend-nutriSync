# NutriSync/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('admin/', admin.site.urls),  # Admin de Django
    path('api/users/', include('users.urls')),  # Rutas de usuarios
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token JWT
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI para documentación
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI para documentación
    path('api/ingredientes/', include('ingredientes.urls')),  # Rutas de ingredientes
    path('api/categorias/', include('categorias.urls')),  # Rutas de categorías
    path('api/recetas/', include('recetas.urls')),  # Rutas de recetas
    path('api/dietas/', include('dieta.urls')),  # Rutas de dietas
    path('api/planes-alimenticios/', include('planes_alimenticios.urls')),  # Rutas de planes alimenticios
]

urlpatterns += staticfiles_urlpatterns()  # Añade las rutas de archivos estáticos


