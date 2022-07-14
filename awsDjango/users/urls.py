from users import views as user_views
from django.urls import path


app_name = 'users'

urlpatterns = [
    path('users/', user_views.users_list, name='users_list'),
    path('users/<slug>/', user_views.profile_view, name='profile_view'),
    path('friends/', user_views.friend_list, name='friend_list'),
    path('users/friend-request/send/<int:id>/', user_views.send_friend_request, name='send_friend_request'),
    path('users/friend-request/cancel/<int:id>/', user_views.cancel_friend_request, name='cancel_friend_request'),
    path('users/friend-request/accept/<int:id>/', user_views.accept_friend_request, name='accept_friend_request'),
    path('users/friend-request/delete/<int:id>/', user_views.delete_friend_request, name='delete_friend_request'),
    path('users/friend/delete/<int:id>/', user_views.delete_friend, name='delete_friend'),
    path('edit-profile/', user_views.edit_profile, name='edit_profile'),
    path('my-profile/', user_views.my_profile, name='my_profile'),
    path('search_users/', user_views.search_users, name='search_users'),
    path('register/', user_views.register, name='register'),
    ]