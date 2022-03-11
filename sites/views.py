from django import views
from django.contrib.auth import get_user_model, forms, views, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views import generic as view

from website.settings import LOGIN_REDIRECT_URL
from website.sites.models import Post

UserModel = get_user_model()


class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'details', 'category']


class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

    def save(self, commit=True):
        return super().save(commit=commit)


class UserRegistrationView(view.CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)

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
    pass


def home(request):
    return render(request, 'home.html')


def post(req):
    return render(req, 'posts.html')


def make_post(request):
    if request.method == 'POST':
        meth = PostsForm(request.POST)
        if meth.is_valid():
            meth.save()
            return redirect('home')
    else:
        meth = PostsForm
    context = {
        'form': meth
    }
    return render(request, 'make-post.html', context)


def about_us(request):
    return render(request, 'about_us.html')
