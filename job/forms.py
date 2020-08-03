from django import forms

from .models import *

class JobFrom(forms.ModelForm):
    class Meta:
        model = Job
        fields  = ["job_title", "description", "job_image", "join_date", "location", "duration", "post_date", "last_date_apply_by",
        "skills_required", "who_can_apply", "other_requirments", "salary","about_company","job_location_place","mobile_number","number_of_openings"]
        # widgets = {
        #     'name' : forms.TextInput(attrs={"class": "form-control"}),
        #     'description':  forms.Textarea(attrs={'class': 'form-control form-control-lg' }),
        #     'image' : forms.FileInput(attrs={"class": "form-control-file"}),
        #     'job_location_place':  forms.TextInput(attrs={'class': 'form-control form-control-lg' }),
        #     'location':  forms.TextInput(attrs={'class': 'form-control form-control-lg' }),
        #     'post_date':  forms.DateInput(attrs={'class': 'form-control form-control-lg' }),
        #     'duration':  forms.TextInput(attrs={'class': 'form-control form-control-lg' }),
        #     'last_date_apply_by':  forms.DateInput(attrs={'class': 'form-control form-control-lg' }),
        #     'about_company':  forms.Textarea(attrs={'class': 'form-control form-control-lg' }),
        #     'skills_required':  forms.Textarea(attrs={'class': 'form-control form-control-lg' }),
        #     'who_can_apply':  forms.Textarea(attrs={'class': 'form-control form-control-lg' }),
        #     'other_requirments':  forms.TextInput(attrs={'class': 'form-control form-control-lg' }),
        #     'salary':  forms.TextInput(attrs={'class': 'form-control form-control-lg' }),
        #     'join_date':  forms.DateInput(attrs={'class': 'form-control form-control-lg' }),
        # }