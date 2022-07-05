from django.contrib import admin
from .models import Post, Comments, Like, PostImage

# admin.site.register(Post)
# admin.site.register(PostImage)
admin.site.register(Comments)
admin.site.register(Like)



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