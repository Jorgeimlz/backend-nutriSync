from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('', views.get_all_users, name='get_all_users'),
    path('<int:user_id>/role/', views.update_user_role, name='update_user_role'),
    path('<int:user_id>/', views.update_user, name='update_user'),
    path('<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('check-admin/', views.check_admin, name='check_admin'),
]
