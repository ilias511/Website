from django.contrib.auth import views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from sites.forms import UserRegistrationForm, PostsForm, ImageForm
from sites.models import Post, AppUser, AppUsername, Images


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
    context = {'post': Post.objects.all().order_by('-id'),}

    return render(request, 'home.html', context)


class AllImages(view.ListView):
    template_name = 'images.html'
    model = Images

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['all_images'] = Images.objects.all()
        return data


class Posts(LoginRequiredMixin, view.ListView):
    login_url = '/login'
    template_name = 'posts.html'
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['users_post'] = Post.objects.filter(user=self.request.user)
        data['users_images'] = Images.objects.filter(user=self.request.user)
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


class PostImage(LoginRequiredMixin, view.CreateView):
    login_url = '/login'
    template_name = 'post-image.html'
    form_class = ImageForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AboutUs(view.TemplateView):
    template_name = 'about_us.html'


class UserProfile(LoginRequiredMixin,view.TemplateView):
    login_url = '/login'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['users_info'] = Post.objects.filter(user=self.request.user).count()
        data['users_images'] = Images.objects.filter(user=self.request.user).count()
        data['total_count'] = data['users_images'] + data['users_info']
        return data


class EditPostsText(view.UpdateView):
    model = Post
    fields = ('title', 'details', 'category')
    template_name = 'edit-post.html'

    def get_success_url(self):
        return reverse_lazy('home')


class DeletePostText(view.DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'delete-posts.html'

class DeletePostImage(view.DeleteView):
    model = Images
    success_url = reverse_lazy('home')
    template_name = 'delete-image.html'