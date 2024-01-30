from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class FitnessInterest(models.Model):
    fitness = models.CharField(max_length=50)

# Links users with their selected interests (many-to-many)
class UserInterest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interest = models.ForeignKey(FitnessInterest, on_delete=models.CASCADE)

class Match(models.Model):
    user1 = models.ForeignKey(Profile, related_name='match_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(Profile, related_name='match_user2', on_delete=models.CASCADE)
    matched_at = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

# Links users with their selected location (many-to-many)
class UserLocation(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)