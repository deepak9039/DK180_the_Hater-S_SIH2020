from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from PIL import Image 
from django.contrib.auth.models import User
from account.models import Company, Profile
# import io
# from django.core.files.uploadedfile import InMemoryUploadedFile

def get_image_filename(instance, filename):
    title = instance.job_title
    slug = slugify(title)
    return "jobImages/%s-%s-%s" % (slug, datetime.now(), filename)

class Job(models.Model):
    company = models.ForeignKey(Company,models.CASCADE)
    job_title = models.CharField(max_length=20)
    description = models.TextField(verbose_name="Job Description ")
    job_image = models.ImageField(upload_to=get_image_filename,verbose_name="Company Image")
    job_location_place = models.CharField(max_length=50,verbose_name="Job Location Place")
    about_company = models.TextField(verbose_name='About Company')
    join_date = models.DateField(verbose_name='Join Date') 
    location = models.CharField(max_length=50,verbose_name='Location')
    duration = models.CharField(max_length=50,verbose_name='Duration')
    post_date = models.DateField(verbose_name='Post Date')
    last_date_apply_by = models.DateField(verbose_name='Last Date Apply By')
    skills_required = models.TextField(verbose_name='Skills Required')
    who_can_apply = models.TextField(verbose_name='Who Can Apply')
    other_requirments = models.CharField(max_length=100,verbose_name='Other Requirments')
    salary = models.FloatField(verbose_name='Salary',default=0)
    applicants = models.ManyToManyField(Profile,blank=True,null= True)
    createation_date = models.DateTimeField(auto_now=True)
    mobile_number = models.CharField(max_length=12,default=0, verbose_name='Mobile No.')
    # number_of_openings = models.CharField(max_length=1000, verbose_name='Number Of Openings')
    number_of_openings = models.IntegerField(max_length=1000,default=0,verbose_name='Number Of Openings')



    def __str__(self):
        return self.job_title

def image_name(instance,filename):
    name = slugify(instance.name)
    return f"city_image/{name}.png"

class City(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to=image_name,default="john-schnobrich-FlPc9_VocJ4-unsplash.jpg")
    
    def __str__(self):
        return self.name    

    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path) # Open image using self

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path