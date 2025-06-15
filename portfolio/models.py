from django.db import models

# Create your models here.
class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100,help_text="eg: fullstack developer")
    bio = models.TextField()
    pp=models.ImageField(upload_to="profile_picture/")
    location = models.CharField(max_length=100,blank=True)
    email= models.EmailField()
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.full_name
    

class Skill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} "


class Project(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    technologies_used = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/', blank=True)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title