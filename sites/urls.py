from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from sites.views import home, Posts, MakePost, AboutUs, UserRegistrationView, LogoutView, UserLoginView, \
    EditPostsText, UserProfile, PostImage, AllImages, DeletePostText, DeletePostImage, remove_user

urlpatterns = [
    path('', home, name='home'),
    path('images/', AllImages.as_view(), name='all images'),
    path('post/', Posts.as_view(), name='posting'),
    path('make-post/', MakePost.as_view(), name='post-make'),
    path('post-image/', PostImage.as_view(), name='post-image'),
    path('about-us/', AboutUs.as_view(), name='about us'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='log in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('edit/<int:pk>/', EditPostsText.as_view(), name='edit post'),
    path('delete/<int:pk>', DeletePostText.as_view(), name='delete post'),
    path('delete/image/<int:pk>', DeletePostImage.as_view(), name='delete image'),
    path('delete/user/<int:pk>',remove_user,name = 'delete user')
]
