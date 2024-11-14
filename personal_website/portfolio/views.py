
from django.http import HttpRequest ,HttpResponse
from django.shortcuts import render
from .models import Project, Skill, Technology  

def project_list(request):
 projects = Project.objects.all().prefetch_related('technologies')
 return render(request, 'portfolio/projects.html', {})

from django.shortcuts import render

def skills_view(request):
     skills = [
    
         {"icon": "fas fa-database", "name": "Data Analysis", "description": "Proficient in analyzing and visualizing data."},
         {"icon": "fab fa-python", "name": "Python", "description": "Experienced in Python for data analysis and development."},
         {"icon": "fas fa-chart-pie", "name": "Power BI", "description": "Skilled in creating interactive dashboards."},
         {"icon": "fas fa-code", "name": "Full Stack Development", "description": "Knowledgeable in front-end and back-end technologies."},
          {"icon": "fas fa-users", "name": "Teamwork", "description": "Effective collaborator in team settings."},
         {"icon": "fas fa-lightbulb", "name": "Creativity", "description": "Innovative problem solver with a creative mindset."},
     ]
    
     context = {
         'skills': skills
      }
     return render(request, 'portfolio/skills.html', context)