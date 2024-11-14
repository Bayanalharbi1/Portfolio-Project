# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
path('skills/', views.skills_view, name='skills_view'),]