from django.contrib import admin

from .models import Topic, Entry, Post, Comment, PostImage

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Comment)


class PostImageAdmin(admin.StackedInline):
    model = PostImage




    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('author','updated_on','created_on')

    readonly_fields = ['updated_on','created_on']
    fieldsets = (
        (None,{'fields':('title','author','status','updated_on','created_on')
        }),
        ('Extended',{
            'fields':('content','image')
        }),
    )
    inlines = [PostImageAdmin]


    
    class Meta:
        model = Post
        
        
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass