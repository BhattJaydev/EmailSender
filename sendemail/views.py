from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from sendemail.models import Customers
from EmailSend import settings

def home(request):
    auth.logout(request)
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        gender = request.POST['g']
        email = request.POST['email']

        print(fname,lname,uname,gender,pwd,email)
        cust = Customers.objects.create(first_name=fname, last_name=lname, username=uname, password=pwd,Email=email,gender=gender)
        cust1 = User.objects.create_user(first_name=fname, last_name=lname, username=uname, password=pwd,email=email)
        cust.save()
        cust1.save()
    return render(request, 'signup.html')

def authlogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
           login(request,user)
           return redirect(reverse('email'))
        else:
            return redirect(reverse('authlogin'))
    return render(request, 'login.html')

@login_required()
def email(request):
    return render(request, 'email.html')

@login_required()
def email_info(request):
    myto = request.POST['to']
    subject = request.POST['subject']
    message = request.POST['message']

    send_mail(subject,message,settings.EMAIL_HOST_USER,[myto],fail_silently=False)
    return render(request, 'emailack.html')