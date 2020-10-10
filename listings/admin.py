from django.contrib import admin
from .models import Listing

# This setting hooks the Listing model to the Admin app
admin.site.register(Listing)


