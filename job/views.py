from django.shortcuts import render,HttpResponse,redirect
from .models import Job
from .forms import *
from django.core.mail import send_mail
import socket
from socket import *    
from django.views.generic.list import ListView
from  django.db.models import Q
from account.views import is_company,is_user_form_filled
from home.models import Notification


class JobListView(ListView):
    model = Job
    context_object_name = "jobs"
    template_name  = "job_feed.html"
    paginate_by = 10
    def get_queryset(self):
        word = self.request.GET["city"]
        word  = word.lower()
        return Job.objects.filter(Q(job_location_place__icontains= word) | Q(job_title= word) ) 

def view_job(request,pk):
    job = Job.objects.get(id =pk)
    param = {
        "job" : job
    }
    return render(request,"job.html",param)

def addjob(request):
    if request.method == "POST":
        form  = JobFrom(request.POST,request.FILES)
        # print(forms)
        if form.is_valid():
            # print("form valid")
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            return redirect("/")
    job_from = JobFrom()
    return render(request,'addJob.html',{"job_form": job_from})

def update_job(request,pk): 
    job = Job.objects.get(id=pk)
    if request.method == "POST":
        form  = JobFrom(request.POST,request.FILES,instance=job )    
        if form.is_valid():
            # print("form valid")
            job = form.save(commit=False)   
            job.company = request.user.company
            job.save()
            return redirect("job",job.id)
    job_from = JobFrom(instance=job)
    return render(request,'addJob.html',{"job_form": job_from,"job":job,"im_updating":True})


def sport(request):
    return render(request,"sport.html")

def delete_job(request,pk): 
    if is_company(request.user): 
        job = Job.objects.get(id=pk)
        job.delete()
        return redirect("profile",request.user.username,)

def apply_job(request,pk):
    if not request.user.is_authenticated:
        return HttpResponse("You are not Autherized Go Back Login First!!<br/> <h1>Accss is Denied</h1>")
        
    user = request.user
    if not is_company(user):
        if not is_user_form_filled(user):
            return redirect("modify_profile")
        else:
            job = Job.objects.get(id=pk)
            job.applicants.add(user.profile)
            job.save()
            Notification.objects.create(
                heading = f"You have Applied For {job.job_title}",
                user = request.user,
                url = f"/job/{job.id}" 
            ).save() 
            send_mail(
                'Congratulations',
                'Hi ' + user.first_name  +'''  Congratulations on making your first application on . We are happy to have you onboard with us! \n
                Now that you have moved a step closer towards securing an job, lets get you acquainted to some 
                of the basic and important guidelines to be followed on job-\n 
                1.job on company are always free. You DO NOT have to pay anything in order to secure an job through us. Please Note: 
                If an organization asks you to pay a security deposit or a fee for the job then,
                please bring this to our attention by visiting the Help Center, so that we can look into
                it and take necessary actions.\n
                2. Please do not accept the job (except NGOs or Campus Ambassador programs) 
                if you are directly hired (without an interview or submitting an assignment) for the job.
                The general process is that the employer takes an interview or gives an assignment. And, on 
                the basis of your performance in that, you are selected for the job or proceed to the next r
                ound of interview. If you do get hired directly then, please bring it to our notice by dropping
                a query from the Help Center.\n
                3. Always ask for an offer letter or an email that confirms your 
                hiring and mentions the terms and conditions of jon from the employer before starting your job. 
                In a campus ambassador program, generally, employers do not give an offer letter. If you receive
                an email with all the details of the program, then that works as well.\n
                4. Never leave the job after accepting the offer extended by the employer. In case of an emergencyor any unavoidable c
                ircumstance you are not able to continue, then please write to the employer regarding 
                the same and elaborate in detail the entire scenario to them. This gesture would help them 
                understand the scenario as well as help them move on to hire the next best candidate quickly.
                \n Great! You are all caught up now and have familiarised yourself with the  general community guidelines. To read the guidelines in detail.\n 
                Now, as your application has been shared with the employer, you must be wondering about the next steps. For th
                at, you need to wait for a few days. If the employer likes your application, he/she will
                get in touch with you within 1-2 weeks and give you further details regarding the job.
                You can also check your application status by logging into your gmail account. \n Tip
                - In case you do not get any response or a status update regarding your application fro
                m the employer within 1-2 weeks of applying and your application status remains Applied, Seen or Under Review then, 
                it is best that you apply for various other jobs that are available on the platform. 
                You may also go through this article to know how you can improve your applications which will, in turn, 
                increase your chances of getting hired.\n All the very best! ''' ,
                'sih202021@gmail.com',
                [ user.email ],
                fail_silently=False,
                ) 
            return redirect("applied_job")
    else:
        return HttpResponse("You are not Autherized <br/> <h1>Accss is Denied</h1>")
    return render(request,"job_view.html")

def applied_job(request):
    return render(request, 'apply_job.html')

def company_application(request):
    return render(request, "company_application.html")
