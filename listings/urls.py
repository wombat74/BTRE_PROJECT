# Created urls.py manually after creating app
from django.urls import path

from . import views
# url will look like: /listings/23
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]