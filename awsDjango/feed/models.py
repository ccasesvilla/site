from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



class Post(models.Model):
	description = models.CharField(max_length=255, blank=True)
	cover_Pic = models.FileField(upload_to='path/to/img', blank=True, default='default.jpg')
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100, blank=True)


     

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
 
class PostImage(models.Model):
	post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='images')
	images = models.FileField(upload_to = 'post_pics', blank=True, default=None,)


	def __str__(self):
		return self.post.description






class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=300, blank=True)
	comment_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
	