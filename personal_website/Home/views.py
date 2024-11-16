from django.shortcuts import render, redirect
from .models import About, Skills, Experience, Service, Contact, Link, Education
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    about = About.objects.first()
    skills = Skills.objects.all()
    return render(request, 'Home/home.html', {'about': about, 'skills': skills})

def about(request: HttpRequest) -> HttpResponse:
    about = About.objects.first()
    links = Link.objects.all()
    return render(request, 'Home/about.html', {'about': about, 'links': links})

def projects(request: HttpRequest) -> HttpResponse:
    services = Service.objects.all()
    return render(request, 'Home/projects.html', {'services': services})

def skills_view(request: HttpRequest) -> HttpResponse:
    skills = Skills.objects.all()
    return render(request, 'Home/skills.html', {'skills': skills})

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect('contact')  # Adjust this if you have a specific URL name for the contact page
    return render(request, 'Home/contact.html')

def experience(request: HttpRequest) -> HttpResponse:
    experiences = Experience.objects.all()
    return render(request, 'Home/experience.html', {'experiences': experiences})

def education(request: HttpRequest) -> HttpResponse:
    education_list = Education.objects.all()
    return render(request, 'Home/education.html', {'education_list': education_list})