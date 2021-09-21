from django.db import models
from django.contrib.auth.models import User





class Topic(models.Model):
    """A topic the user is learning/writing about."""
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        """Return a string representation of the model."""
        
        return self.text




    

class Entry(models.Model):
    """Something specific learned about a topic."""
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model."""
            
        return '%s  |   %s' % (self.topic, self.text)
     
from django.utils.text import slugify 
from django.dispatch import receiver
from django.db.models.signals import pre_save

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
from autoslug import AutoSlugField
from django.db import models
from tinymce import models as tinymce_models
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.FileField(blank=True, default='default.png')


    class Meta:
        ordering = ['-created_on']




    def __str__(self):
        
        return self.title 
    
    
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=1, on_delete=models.CASCADE, blank=False)
    images = models.FileField(upload_to ='post_pics', blank=True, default=None)
    
    def __str__(self):
        return self.post.title
    
       
      


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)