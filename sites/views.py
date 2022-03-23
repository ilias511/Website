from django import views
from django.contrib.auth import get_user_model, forms, views, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
    context = {'post': Post.objects.all().order_by('-id')}

    return render(request, 'home.html', context)


class Posts(LoginRequiredMixin, view.ListView):
    login_url = '/login'
    template_name = 'posts.html'
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['users_post'] = Post.objects.filter(user=self.request.user)
        return data


# def posts(request):
#     if request.user:
#         return redirect('log in')
#     user_posts = Post.objects.filter(user=request.user)
#     context = {'post': user_posts}
#     return render(request, 'posts.html', context)


class MakePost(LoginRequiredMixin, view.CreateView):
    login_url = '/login'
    template_name = 'make-post.html'
    form_class = PostsForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AboutUs(view.TemplateView):
    template_name = 'about_us.html'

