from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from website.sites.views import home, Posts,MakePost, AboutUs, UserRegistrationView, LogoutView, UserLoginView

urlpatterns = [
    path('', home, name='home'),
    path('post/',Posts.as_view(), name='posting'),
    path('make-post/', MakePost.as_view(), name='post-make'),
    path('about-us/', AboutUs.as_view(), name='about us'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(),name = 'log in'),
    path('logout/',LogoutView.as_view(),name = 'logout')
]
