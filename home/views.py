from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from job.models import Job,City
import PIL
from  django.db.models import Q
from django.core.mail import send_mail
import socket
from .models import Notification
# Creimportate your views here.
def home(request):
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



    # return render(request,'search.html')
    # print('kuchh nhi')
    # return redirect("/")
