from django.shortcuts import render
from .models import Listing
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Pakage, Package
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.
def index(request):
    # select * from listing WHERE 'is_published'=TRUE ODER BY 'list_date' DESC
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # for pagination
    paginator = Paginator(listings, 6)
    # Paginator.get_page(number) -> Returns a Page object with the given 1-based index, while also handling out of range and invalid page numbers.

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings/listings.html', {'listings': paged_listings})


def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)
    if request.user.is_authenticated:

        user_id = request.user.id
        # print(user_id)

        # SELECT COUNT()FROM contact WHERE WHERE 'userid'= user_id
        contact_count = Contact.objects.filter(user_id=user_id).count()
        # print(contact_count)
        count = str(contact_count)
        package = Pakage.objects.filter(user_id=user_id)

        package_id = package[0].pakage
        admin_package = Package.objects.filter(id=package_id)
        package_count = admin_package[0].proview
        # {% if count < package_count %}
        # 0<5 ,1<5,2<5,3<5,4<5
        # else:
        context = {
            'listing': listing,
            'count': count,
            'package_count': package_count,
            # 'newpackage': newpackage

        }
    else:
        context = {
            'listing': listing,
            # 'count': count,
            # 'package_count': package_count

        }

    return render(request, 'listings/listing.html', context)


def search(request):
    # select * from listing ODER BY 'list_date' DESC
    queryset_list = Listing.objects.order_by('-list_date')
   # return HttpResponse(queryset_list.query)

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
           # SELECT descrpitions FROM listing WHERE descriptions CONTAINS 'word1 word2 word3...'
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
            # return HttpResponse(queryset_list.query)

    # city
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            # SELECT city FROM listing WHERE 'city'= 'city'
            queryset_list = queryset_list.filter(city__iexact=city)

    # city
    if 'state' in request.GET:
        state = request.GET['state']

        if state:
            # SELECT state FROM listing WHERE 'state'= 'state'
            queryset_list = queryset_list.filter(state__iexact=state)

    # city
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']

        if bedrooms:
            # SELECT bedrooms FROM listing WHERE 'bedrooms'= 'bedrooms'
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

     # price
    if 'price' in request.GET:
        price = request.GET['price']

        if price:
            # SELECT price FROM listing WHERE 'price'= 'price'
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
