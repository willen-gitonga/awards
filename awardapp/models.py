from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    bio = models.TextField(max_length = 50,null = True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.comment

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, search_term):
        userprofile = Profile.objects.filter(user__icontains = search_term)
        return userprofile

class Project(models.Model):
    image = models.ImageField(upload_to = 'images/')
    project_name = models.CharField(max_length =10)
    project_url = models.CharField(max_length =50)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def save_project(self):
        self.save()
    
   
    @classmethod
    def get_all_projects(cls):
        project = cls.objects.all()
        return project

    @classmethod
    def find_project_id(cls, id):
        project_result = cls.objects.get(project_id=id)
        return project_result

class Rate(models.Model):
    project = models.ForeignKey('Project')
    design = models.CharField(max_length=30)
    usability = models.CharField(max_length=8)
    creativity = models.CharField(max_length=8,blank=True,null=True)
    user = models.ForeignKey(User)
    

    def __str__(self):
        return self.design


    def save_rate(self):
        self.save()

     
    @classmethod
    def get_all_rating(cls):
        ratings = cls.objects.all()
        return ratings
