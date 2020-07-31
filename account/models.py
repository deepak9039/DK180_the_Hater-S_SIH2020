from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
# from job.models import Job


def get_image_name(instance, filename):
    title = instance.user.username
    slug = slugify(title)
    return "profileImages/%s-%s-%s" % (slug, datetime.now(), filename)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=15,verbose_name="Phone Number")
    intrest = models.CharField(max_length=20)
    skill = models.TextField(verbose_name="Add Skills")
    certificate = models.TextField()
    profile_pic = models.ImageField(upload_to=get_image_name,verbose_name="Profile Picture",blank=True,null=True)
    is_filled = models.BooleanField(default=False)
    # Applied_job = models.ManyToManyField(to=Job,blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # name = models.CharField(max_length=20)
    image = models.FileField(upload_to=f"company-img/")
    description = models.TextField()
    
    def __str__(self):
        return str(self.user)       