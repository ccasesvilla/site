from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings


STATUS = (
    (0, "Regular User"),
    (1, "Author")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20, blank = True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    slug = AutoSlugField(populate_from = 'user')
    status = models.IntegerField(choices=STATUS, default=0)
    bio = models.CharField(max_length=300, blank = True)
    description = models.TextField(max_length=1000, blank = True)
    interests = models.TextField(max_length=1000, blank = True)
    friends = models.ManyToManyField("Profile", blank = True)
    #fav_authors = models.ManyToManyField("Profile", blank = True)


    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return "/users/{}".format(self.slug)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.FileField(upload_to='profile_album', blank=True)

    def __str__(self):
        return self.profile.user


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)