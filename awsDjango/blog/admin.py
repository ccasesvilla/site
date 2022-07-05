from django.contrib import admin

from .models import Topic, Entry, Post, Comment, PostImage

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Comment)


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    
    class Meta:
        model = Post
        
        
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass