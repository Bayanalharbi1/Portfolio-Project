from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('data', 'Data Analysis'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
class PersonalInfo(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/')