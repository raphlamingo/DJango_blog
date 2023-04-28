from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    first_name= models.CharField( max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.CharField(max_length=30, unique=True)
    about_me= models.TextField(null=False, blank=False)
    profile_picture= models.ImageField(null=True, blank=True, default='andrew-neel-cckf4TsHAuw-unsplash.jpg')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.email

class Posts(models.Model):
    writer= models.ForeignKey(Users, on_delete=models.CASCADE)
    title= models.CharField(max_length=40)
    content= models.TextField(null=False, blank=False)
    created= models.DateField(auto_now_add=True)
    vote_ratio= models.IntegerField(default=0, null=True, blank=True)
    upload_picture= models.ImageField(null=False, blank=False, upload_to='profile/')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

class Review(models.Model):
    vote_type = (
        ('up','up_vote'),
        ('down', 'down_vote')
    )
    post= models.ForeignKey(Posts, on_delete=models.CASCADE)
    review= models.TextField(null=True,blank=True)
    value= models.CharField(max_length=100, choices=vote_type)
    def __str__(self):
        return self.value
