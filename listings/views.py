from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

def index(request):
    # Grab all of the listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # "-" sets it as descending

    paginator = Paginator(listings, 6) # number of items per page
    page = request.GET.get('page') # grab the "page" url parameter
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id): # must add listing_id so that we can reference the id
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'listings/search.html', context)
