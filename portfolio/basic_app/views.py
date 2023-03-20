from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    myinfo = models.PersonalInfo.objects.all()
    myabout = models.About.objects.all()
    myskills = models.Projects.objects.all()
    skills = models.Skills.objects.all()
    context = {
        'info':myinfo,
        'about':myabout,
        'skills':myskills,
        'know':skills
    }
    return render(request,'home.html',context)