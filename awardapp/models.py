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
    

    def delete_profile(self):
        self.delete()

   
class Project(models.Model):
    image = models.ImageField(upload_to = 'images/')
    project_name = models.CharField(max_length =10)
    project_url = models.CharField(max_length =50)
    description =models.CharField(max_length =100)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
    
   
  
# START OF THE CLASSES FOR RATING 

class DesignRating(models.Model):
   
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    project = models.ForeignKey('Project')
    user = models.ForeignKey(User)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)

    def __str__(self):
        return self.rating

    def save_designrating(self):
        self.save()
    
    def delete_designrating(self):
        self.delete()
    
class UsabilityRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    project = models.ForeignKey('Project')
    user = models.ForeignKey(User)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    
    def __str__(self):
        return self.rating

    def save_usabilityrating(self):
        self.save()
    
    def delete_usabilityrating(self):
        self.delete()

class ContentRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    project = models.ForeignKey('Project')
    user = models.ForeignKey(User)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)

    def __str__(self):
        return self.rating

    def save_contentrating(self):
        self.save()
    
    def delete_contentrating(self):
        self.delete()
    
