from django.contrib import admin
from .models import Realtor

# This setting hooks the Realtor model to the Admin app
admin.site.register(Realtor)
