from django.shortcuts import render, HttpResponse,redirect
from django.contrib import auth
from django.contrib import messages
from django.core.mail import send_mail
import socket
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Profile
import requests
import json
import urllib.request

# from .models import Company

def is_user_form_filled(user):
    try:
        profile = user.company
        return True
    except:
        try:
            profile = user.profile
            return True
        except:
            return False
        
def is_company(user):
    try:
        user.company
        return True
    except:
        return False
def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Recaptcha stuff
        clientkey = request.POST["g-recaptcha-response"]
        secretkey = '6LcRvrcZAAAAAA4mf4Tto0cbhX-K32XrSPl_jMJb'  # secret key 
        captchaData = {
            'secret': secretkey,
            'response': clientkey,
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data= captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('our seccess is: ', verify)
        
        # signup email sender
        send_mail('Signup ','Hello ' + name +'  Congratulations! You have successfully registered Thank you for the job in exploring career opportunities with Govt. ,Wish you the Best of Luck for the selection process.' ,'sih202021@gmail.com',
                    [ email ],
                    socket.getaddrinfo('localhost', 8080),
                    # fail_silently=False,
                )

        try:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name)
            user.save()
            auth.login(request,user)
            if verify:
                return redirect("modify_profile")
            else:
                return HttpResponse('<script> alert("Please fill google captch") </script> ')
    

        except:
            return HttpResponse("User name is Already Exist")
        return redirect("profile",username)
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["loginusername"]
        password = request.POST["loginpassword"]
        user = auth.authenticate(username=username,password=password)
        

        if user is None:
            return HttpResponse("Invalid Username or Password")
        auth.login(request,user)
        messages.success(request,f'you are login successfully {username}')
        if not is_user_form_filled(user):
            return redirect("modify_profile")
            
        return redirect("profile",username)   
    return render(request,'profile.html')

def profile(request,username):
    user = User.objects.get(username=username)
    param = {
        "user" : user
    }
    if is_company(user):    
        return render(request,"company_profile.html",param)    
    return render(request,"profile.html",param)



def logout(request):
    
    auth.logout(request)
    messages.success(request,f'you are logout successfully')
    return redirect("/")

@login_required
def modify_profile(request):
    if request.method == "POST":
        try:
            user = Profile.objects.get(user=request.user)
            form = ProfileForm(request.POST, request.FILES,instance=user)
        except:
            # user = Profile.objects.get(user=request.user)
            form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # print("v")
            profile = form.save(commit=False)
            profile.user = request.user

            request.user.username = request.POST["username"]
            request.user.first_name = request.POST["firstname"]
            request.user.last_name = request.POST["lastname"]
            request.user.email = request.POST["mail"]
            request.user.save()

            profile.is_filled = True
            profile.save()
            return redirect("profile",request.user.username)
    try:
        user = Profile.objects.get(user=request.user)
        profile = ProfileForm(instance = user)
    except:
        profile = ProfileForm()
    return render(request,"modify_profile.html",{"form" : profile})

def companysignup(request):
    if request.method == "POST":
        # print("few;jmfreiuh")
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        # Recaptcha stuff
        clientkey = request.POST["g-recaptcha-response"]
        secretkey = '6LcRvrcZAAAAAA4mf4Tto0cbhX-K32XrSPl_jMJb'
        captchaData = {
            'secret': secretkey,
            'response': clientkey,
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data= captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('our seccess is: ', verify)
        form = CompanySignupForm(request.POST,request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            send_mail(
                'Subject ',
                'Hello ' + name + ' Thanks For Signup Congratulations! You have successfully registered on the NextStep Portal. Follow the instructions given below to fill in the Application Form. 1. Login the system using username or password 2. Click the Add Button then form will open and you can add job. 3.After add job you get a email your job added successfully.',
                'sih202021@gmail.com',
                [ email ],
                socket.getaddrinfo('localhost', 8080),
                # fail_silently=False,
            )
            try:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=name)
                user.save()
                company.user = user
                company.save()
                auth.login(request,user)
                

            except:
                return HttpResponse("User name is Already Exist")
            return redirect("profile",username)
    
    return render(request,'companysignup.html',{"forms": CompanySignupForm()})

def company_update(request):
    if request.method == "POST":
        user = request.user

        user.first_name = request.POST.get("company_name",None)
        user.username = request.POST.get("username",None)
        user.email = request.POST.get("email",None)
        user.company.description = request.POST.get("desc",None)
        user.save()
        user.company.save()

        return redirect("profile",request.user.username)
    return render(request,'company_update.html')

# def password_reset(request):
#     return render(request,'password_reset.html')