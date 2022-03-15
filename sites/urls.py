from django.contrib import admin
from django.urls import path

from website.sites.views import home, post,MakePost, about_us, UserRegistrationView, LogoutView, UserLoginView

urlpatterns = [
    path('', home, name='home'),
    path('post/', post, name='posting'),
    path('make-post/', MakePost.as_view(), name='post-make'),
    path('about-us/', about_us, name='about us'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(),name = 'log in'),
    path('logout/',LogoutView.as_view(),name = 'logout')
]
