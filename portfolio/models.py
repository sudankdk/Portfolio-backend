from django.db import models

# Create your models here.
class Portfolio(models.Model):
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