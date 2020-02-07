
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="Users biography", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    

     
    
class Post(models.Model):
    caption = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'posts/')

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')


    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f'{self.user.name} Post'
    
class Likes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    class Meta:
        db_table = 'likes'
