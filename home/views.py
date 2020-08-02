from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from django.core import serializers


from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from job.models import Job,City
import PIL
from  django.db.models import Q
from django.core.mail import send_mail
import socket
from .models import Notification
from account.views import is_company
# Creimportate your views here.
def home(request):
    if request.user.is_authenticated : # refresh
        user = request.user
        if is_company(user):
            job_detail = user.company.job_set.all()
        else:
            skill = user.profile.skill
            intrest = user.profile.intrest

            job_detail = Job.objects.filter(Q(job_title__icontains=skill) | Q(skills_required__icontains=skill) | Q(skills_required__icontains=intrest))
    else:
        job_detail = Job.objects.all().order_by("?")
    city_list = City.objects.all().order_by("-id")
    
    
    try:
        newC = job_detail[3:]
    except:
        newC = None      
    param = {
        # "jobCard": job_detail[:5],
        # "jobcrouselactive" : job_detail[:5],
        "jobNextCrousel" : newC,
        "cities" : city_list,
        "jobs": job_detail[:5],
        # "jobs_view": job_detail,

    }
    return render(request,'home.html',param)
def subscribe(request):
    email1 = request.GET["subscriber_email"]
    # path = request.GET["redirect"]
    # print(path)
    send_mail(
                    'Subject ',
                    'thanks for subscibe ',
                    'sih202021@gmail.com',
                    [ email1 ],
                    socket.getaddrinfo('localhost', 8080),
                    # fail_silently=False,
                )
    return redirect("/")

def search(request):
    if request.method=='POST':
        search1 = request.POST['search'] 
        if search1:
            match = Job.objects.filter(Q(job_title__icontains=search1) | Q(job_location_place__icontains=search1))
            
            if match:
                return render(request,'search.html', {'jobs':match})
            else:
                return render(request,'search.html')
        else:
            return redirect("/")
    else:
        return redirect("/")


def notification(request):
    return render(request,'notification.html')

def makeRead(request):
    pk = request.GET["id"]
    notify = Notification.objects.get(id=pk)
    notify.seen = True
    notify.save()
    return HttpResponse("done")


# profile based job recoommed logic

def proflieJobMatchig(request):
        get_skills = request.GET['skills_match'] 
        if get_skills:
            match_profile = Job.objects.filter(Q(skill__icontains=get_skills) | Q(intrest__icontains=get_skills))
            return JsonResponse(serializers.serialize(format="json",queryset=get_skills),safe=False)
            print(match_profile)
        else:
            return render(request,'home.html')

            # ab eske bas pas json wala kam karna ha bas