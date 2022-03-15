from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField

from website.sites.models import Post, AppUsername

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    username = CharField(max_length=25)
    age = CharField(max_length=2)

    class Meta:
        model = UserModel
        fields = ('email',)

    # just to hide validation messages
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for field_name in ['email', 'password1', 'password2', 'username']:
            self.fields[field_name].help_text = None

    def clean_first_name(self):
        return self.cleaned_data['username', 'age']

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = AppUsername(
            username=self.cleaned_data['username'],
            age=self.cleaned_data['age'],
            user=user
        )
        if commit:
            profile.save()
        return user


class PostsForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        post = super().save(commit=False)
        post.user = self.user
        if commit:
            post.save()
        return post

    class Meta:
        model = Post
        fields = ('title', 'details', 'category')
