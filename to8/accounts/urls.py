from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_user, name='register'),
    path('login', views.login_user, name='user_login'),
    path('logout', views.logout, name='user_logout'),
]
