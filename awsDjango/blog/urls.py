from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static





from django.conf.urls import url


app_name = 'blog'
urlpatterns = [

    path('blog_list/', views.Blog_List1, name='blog_list'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('<slug:slug>/', views.blog_detail, name="blog_detail"),
    ] 
    # id we are in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
