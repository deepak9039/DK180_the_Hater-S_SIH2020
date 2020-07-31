from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic", "phoneNo", "intrest","skill","certificate"]
        widgets = {
            'phoneNo' : forms.TextInput(attrs={"class": "form-control col-4"}),
            'intrest' : forms.Textarea(attrs={"class": "form-control", "style":"height: 108px;"}),
            'skill' : forms.Textarea(attrs={"class": "form-control", "style":"height: 108px;"}),
            'certificate' : forms.Textarea(attrs={"class": "form-control", "style":"height: 108px;",  }),
        }

class CompanySignupForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['image','description']
        widgets = {
            "image" : forms.FileInput(attrs={"class":"form-control"}),
            "description" : forms.Textarea(attrs={"class":"form-control","rows":"4"})
        }