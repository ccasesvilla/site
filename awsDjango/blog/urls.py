from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url




from django.conf.urls import url


app_name = 'blog'
urlpatterns = [

    path('blog_list/', views.Blog_List1, name='blog_list'),
    path('blog_list/', views.postimage_list, name='blog_list'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('search_results/', views.search, name='search_results'),
    path('show_results/<entry_id>', views.show_results, name='show_results'),	
    path('topics/', views.topics, name='topics'),
    #Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    url(r'^delete/(?P<slug>\d+)/$', views.delete, name='delete'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
    path('blog_detail/', views.blog_detail, name='blog_detail'), 
    path('<slug:slug>/', views.blog_detail, name="blog_detail"),        
    ] 
    # id we are in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
