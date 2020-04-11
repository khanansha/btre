
from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth.models import User
from contacts.models import Contact
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text

# Create your views here.


def register(request):
    if request.method == 'POST':

    # Get form values

        first_name = request.POST['first_name']

        last_name = request.POST['last_name']

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        password2 = request.POST['password2']



    # Check if passwords match

        if password == password2:
        # Check username
            if User.objects.filter(username=username).exists():

                messages.error(request, 'That username is taken')

                return redirect('register')

            else:

                if User.objects.filter(email=email).exists():

                    messages.error(request, 'That email is being used')

                    return redirect('register')

                else:

                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)

         

                    user.save()

                    messages.success(request, 'You are now registered and can log in')

                    return redirect('login')

        else:

            messages.error(request, 'Passwords do not match')

            return redirect('register')

    else:

        return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        

        if user is not None:

            auth.login(request, user)

            messages.success(request, 'You are now logged in')

            return redirect('dashboard')

        else:

            messages.error(request, 'Invalid credentials')

            return redirect('login')

    else:

        return render(request, 'accounts/login.html')
   

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        messages.success(request, 'You are now logged out')

        return redirect('index')



def dashboard(request):

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)



    context = {

    'contacts': user_contacts

    }

    return render(request, 'accounts/dashboard.html', context)

def rest_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        randotp = get_random_string(6, allowed_chars='0123456789')
        if User.objects.filter(email=email).exists():
            #UPDATE User table SET password = 'randopt' WHERE email='email'
            #u=User.objects.filter(email=email).update(password=randotp)
            u = User.objects.get(email=email)
            u.set_password(randotp)
            u.save()
            current_site = get_current_site(request)
            subject, from_email, to = 'reset password', 'anjumkhan88987@gmail.com', email
            text_content = ''
            # html_content = 'Please activate your account <a href="http://' + \
            # current_site.domain + '/activate_email?e='+to+'" target="_blank">Click here</a>'
            html_content = ' Hii your new password is ' + randotp + ' now you can login with this password'
            msg = EmailMultiAlternatives(
                subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'we have sent you an email please follow the instructions')
            return redirect('login')
        else: 
            messages.error(request, 'Invaild email')
            return redirect('rest_password')
    return render (request,'accounts/forget_password.html')