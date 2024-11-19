from django.shortcuts import render, redirect
from .models import Skill, Project
from .forms import SkillForm, ProjectForm

def dashboard_home(request):
    skills = Skill.objects.all()  
    projects = Project.objects.all()  
    return render(request, 'dashboard/dashboard.html', {'skills': skills, 'projects': projects})

def skills_dashboard(request):
    skills = Skill.objects.all()
    return render(request, 'dashboard/skills_dashboard.html', {'skills': skills})

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills_dashboard')
    else:
        form = SkillForm()
    return render(request, 'dashboard/skill_form.html', {'form': form})

def edit_skill(request, pk):
    skill = Skill.objects.get(pk=pk)  
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skills_dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'dashboard/skill_form.html', {'form': form})

def delete_skill(request, pk):
    skill = Skill.objects.get(pk=pk)  
    if request.method == 'POST':
        skill.delete()
        return redirect('skills_dashboard')
    return render(request, 'dashboard/delete_confirm.html', {'item': skill})

# Projects Views
def projects_dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/projects_dashboard.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_dashboard')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/project_form.html', {'form': form})

def edit_project(request, pk):
    project = Project.objects.get(pk=pk)  
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/project_form.html', {'form': form})

def delete_project(request, pk):
    project = Project.objects.get(pk=pk)  
    if request.method == 'POST':
        project.delete()
        return redirect('projects_dashboard')
    return render(request, 'dashboard/delete_confirm.html', {'item': project})