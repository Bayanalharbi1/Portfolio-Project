# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),  
    path('skills/', views.skills_dashboard, name='skills_dashboard'),
    path('skills/add/', views.add_skill, name='add_skill'),
    path('skills/edit/<int:pk>/', views.edit_skill, name='edit_skill'),
    path('skills/delete/<int:pk>/', views.delete_skill, name='delete_skill'),

    # Projects URLs
    path('projects/', views.projects_dashboard, name='projects_dashboard'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/edit/<int:pk>/', views.edit_project, name='edit_project'),
    path('projects/delete/<int:pk>/', views.delete_project, name='delete_project'),
]