from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import *


def home(request):
    return render( request, 'home.html' )


def about(request):
    return render( request, 'about.html' )


def services(request):
    return render( request, 'services.html' )


def air(request):
    return render( request, 'air.html' )


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm( data=request.POST )
        if form.is_valid():
            contact_name = request.POST.get( 'contact_name', '' )
            contact_email = request.POST.get( 'contact_email', '' )
            form_content = request.POST.get( 'content', '' )

            send_mail(
                'Sales Cargo',
                form_content,
                contact_email,
                ['info@wilpalinternationallogistics.com', 'paul@wilpalinternationallogistics.com'],
                fail_silently=True,
            )
            messages.success( request, 'The email has been sent successfully.' )
            return HttpResponseRedirect( request.META.get( 'HTTP_REFERER' ) )
        else:
            messages.warning( request, 'Something is not right. Please try again' )
    return render( request, 'contact.html', locals() )
