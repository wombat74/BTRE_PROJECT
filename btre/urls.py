# This is the routing file.
# URL path/, (ViewMethod)
# You can also link to URLs in other apps

from django.contrib import admin
from django.urls import path, include
# Add below to support "static(settings..."
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), # linking to the urls.py of the pages app
    path('listings/', include('listings.urls')), # linking to the urls.py of the pages app
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add this to have access to images
