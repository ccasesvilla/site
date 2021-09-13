from django.contrib import admin
from .models import Profile, FriendRequest, ProfileImage

admin.site.register(Profile)
admin.site.register(ProfileImage)
admin.site.register(FriendRequest)