# Created urls.py manually after creating app
from django.urls import path

from . import views
# url will look like: /listings/23
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]