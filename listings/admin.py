from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin): # This allows us to customize the admin page
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') # This adds fields to the table
    list_display_links = ('id', 'title') # This enables the id and title to be hyperlinks
    list_filter = ('realtor',) # This makes any field a filter
    list_editable = ('is_published',) # This makes a field editable
    search_fields = ('title', 'desctiption', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin) # This setting hooks the Listing model to the Admin app


