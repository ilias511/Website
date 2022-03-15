from django import views
from django.contrib.auth import get_user_model, forms, views, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views import generic as view

from website.settings import LOGIN_REDIRECT_URL
from website.sites.forms import UserRegistrationForm, PostsForm
from website.sites.models import Post, AppUser


class UserRegistrationView(view.CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(views.LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)

        if next:
            return next
        return reverse_lazy('home')


class LogoutView(views.LogoutView):
    next_page = 'home'


def home(request):
    context = {'post': Post.objects.all()}

    return render(request, 'home.html',context)


def post(request):
    user_posts = Post.objects.filter(user=request.user)
    context = {'post': user_posts}
    return render(request, 'posts.html',context)


class MakePost(view.CreateView):
    template_name = 'make-post.html'
    form_class = PostsForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


# def make_post(request):
#     if request.method == 'POST':
#         meth = PostsForm(request.POST)
#         if meth.is_valid():
#             meth.save()
#             return redirect('home')
#     else:
#         meth = PostsForm
#     context = {
#         'form': meth
#     }
#     return render(request, 'make-post.html', context)


def about_us(request):
    return render(request, 'about_us.html')
