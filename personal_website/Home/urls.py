from django.urls import path
from . import views
app_name = 'Home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills_view, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
]