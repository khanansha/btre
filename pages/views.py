
#from .forms import SignupForm 
from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect ,HttpResponse
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    # SELECT * FROM `listings_listing` WHERE `is_published` = True ORDER BY `list_date` DESC LIMIT 3

    # return HttpResponse(listings.query)

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    

    return render(request, 'pages/index.html', context)

# Create your views here.


def about(request):
    #select * from realtor ORDER BY `hire_date` DESC
    realtors = Realtor.objects.order_by('-hire_date')
    #select * from realtor WHERE 'is_mvp'=True
    mvp_realtors= Realtor.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,


    }

    return render(request,'pages/about.html',context)
