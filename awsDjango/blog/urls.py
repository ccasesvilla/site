from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import UserBlogListView
from django.conf.urls import url


app_name = 'blog'
urlpatterns = [
    path('blog_list/', views.Blog_List1, name='blog_list'),
    path('blog_list/', views.postimage_list, name='blog_list'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('search_results/', views.search, name='search_results'),
    path('blog_draft/', views.blog_draft, name='blog_draft'),
    path('edit_blog/<int:entry_id>/', views.edit_blog, name='edit_blog'),
	path('blog/<int:pk>/delete/', views.blog_delete, name='blog-delete'),
	path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    url(r'^delete/(?P<slug>\d+)/$', views.delete, name='delete'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
    path('blog_detail/', views.blog_detail, name='blog_detail'), 
    path('<slug:slug>/', views.blog_detail, name="blog_detail"),
	path('user_blogs/<str:username>', UserBlogListView.as_view(), name='user-blogs'),    
    path('tinymce/', include('tinymce.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)