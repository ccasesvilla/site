from django.contrib import admin
from .models import Profile, FriendRequest, ProfileImage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (None, {'fields': ('user','image','last_name','first_name','status')
        }),
        ('Extended', {
            'fields':('bio','description','interests','friends')
        }),
    )

    list_filter = ('status','user','last_name','first_name')



#admin.site.register(Profile)


admin.site.register(ProfileImage)


admin.site.register(FriendRequest)

