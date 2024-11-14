from django.shortcuts import render
from .models import PersonalInfo, Skill
from portfolio.models import Project


def home(request):
    info = PersonalInfo.objects.first()
    recent_projects = Project.objects.all()[:3]  
    context = {
        'info': info,
        'recent_projects': recent_projects,  
    }
    return render(request, 'main/home.html', context)
def about(request):
    info = PersonalInfo.objects.first()
    context = {
        'info': info,
    }
    return render(request, 'main/about.html', context)

def skills(request):
    frontend_skills = Skill.objects.filter(category='frontend')
    backend_skills = Skill.objects.filter(category='backend')
    data_skills = Skill.objects.filter(category='data')
    context = {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'data_skills': data_skills,
    }
    return render(request, 'main/skills.html', context)

def contact(request):
    return render(request, 'main/contact.html')