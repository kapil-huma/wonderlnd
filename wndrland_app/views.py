from django.shortcuts import render, redirect
from .models import Subscriber_newsletter,contact_us
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_subscriber = Subscriber_newsletter(email=email)
        new_subscriber.save()
        subject ="Thankyou for subscribing"
        message = " You are successfully subscribed to our new updates"
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email])
        subject1 ="New Subscriber"
        message1 = str(email) +"New user subscribed"
        send_mail(subject1, message1, email, [from_email])
    return render(request, 'home.html')

def about(request):
    return render(request, 'roadmap.html')

def vision(request):
    return render(request, 'our-vision.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        review = request.POST.get('review')
        new_contact = contact_us(name=fname,email=email, address=address, phone=phone, review=review)
        new_contact.save()
        subject ="Contact Us"
        message = "Thankyou for contacting us"
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email])
        subject1 ="Contact Us Query"
        ctx = {
                'email': email,
                'fname':fname,
                'phone':phone,
                'address':address,
                'review':review
            }
        message1 =get_template('mail.html').render(ctx)
        send_mail(subject1, message1, email, [from_email])

    return render(request, 'contact.html')
