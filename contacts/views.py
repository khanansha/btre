from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from accounts.models import Pakage
# Create your views here.
# @login_required(login_url="/accounts/register")


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']

        listing = request.POST['listing']

        name = request.POST['name']

        email = request.POST['email']

        phone = request.POST['phone']

        message = request.POST['message']

        user_id = request.POST['user_id']

        realtor_email = request.POST['realtor_email']
        #  Check if user has made inquiry already

        if request.user.is_authenticated:

            user_id = request.user.id

            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)

            if has_contacted:

                messages.error(
                    request, 'You have already made an inquiry for this listing')

                return redirect('/listings/'+listing_id)
            # fetch package FILTER (user_id= user_id)
            #contact_count = Contact.objects.filter(user_id=user_id).count()
            #count = str(contact_count)
            # print(count)
            #package = Pakage.objects.filter(user_id=user_id)
            #package_count = package[0].pakage
            # print(package_count)
            # get total number of enquiry count
            # if count < package_count:
              # if 0< 2 (true)
              # ==
              # !=
              # <= less than equal to
              # >= greater than equal to
              # <
              # >
            contact = Contact(listing=listing, listing_id=listing_id, name=name,
                              email=email, phone=phone, message=message, user_id=user_id)

            contact.save()

    # Send email

            send_mail('Property Listing Inquiry', 'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info', 'anjumkhan88987@gmail.com', [realtor_email, email],
                      fail_silently=False)
            messages.success(
                request, 'Your request has been submitted, a realtor will get back to you soon')

            return redirect('/listings/'+listing_id)
            # else:
            #     messages.error(
            #         request, 'expired')

            #     return redirect('/listings/'+listing_id)

    # CONTACT.SAVE
    # SEND EMAIL
    # else
    # MESSAGE.ERROR
    # REDIRECT(LISTING)
    # contact = Contact(listing=listing, listing_id=listing_id, name=name,
     #                 email=email, phone=phone, message=message, user_id=user_id)

    # contact.save()
    # Send email

    # send_mail('Property Listing Inquiry', 'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info', 'anjumkhan88987@gmail.com', [realtor_email, email],
     #         fail_silently=False)

    # messages.success(
     #   request, 'Your request has been submitted, a realtor will get back to you soon')

    # return redirect('/listings/'+listing_id)
