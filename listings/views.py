from django.shortcuts import render
from .models import Listing
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    #select * from listing WHERE 'is_published'=TRUE ODER BY 'list_date' DESC
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # for pagination
    paginator = Paginator(listings, 6)
    #Paginator.get_page(number) -> Returns a Page object with the given 1-based index, while also handling out of range and invalid page numbers.

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings/listings.html', {'listings':paged_listings})


def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    return render(request,'listings/listing.html',{'listing':listing})

def search(request):
    # select * from listing ODER BY 'list_date' DESC
    queryset_list = Listing.objects.order_by('-list_date')
   # return HttpResponse(queryset_list.query)

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
           #SELECT descrpitions FROM listing WHERE descriptions CONTAINS 'word1 word2 word3...'
            queryset_list = queryset_list.filter(description__icontains=keywords)
            #return HttpResponse(queryset_list.query)

    #city
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            #SELECT city FROM listing WHERE 'city'= 'city'
            queryset_list = queryset_list.filter(city__iexact=city)

    #city
    if 'state' in request.GET:
        state = request.GET['state']

        if state:
            #SELECT state FROM listing WHERE 'state'= 'state'
            queryset_list = queryset_list.filter(state__iexact=state)

    
    #city
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']

        if bedrooms:
            #SELECT bedrooms FROM listing WHERE 'bedrooms'= 'bedrooms'
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

     #price
    if 'price' in request.GET:
        price = request.GET['price']

        if price:
            #SELECT price FROM listing WHERE 'price'= 'price'
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    
    return render(request,'listings/search.html',context)    
