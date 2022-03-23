from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, DateField

from website.sites.models import Post, AppUsername

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    username = CharField(max_length=20)
    date_of_birth = DateField()

    class Meta:
        model = UserModel
        fields = ('email',)

    # just to hide validation messages
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for field_name in ['email', 'password1', 'password2', 'username']:
            self.fields[field_name].help_text = None

    # save returns all the data when we finish a form
    # in that way we take the user, which is the logged user
    # then we create a profile with this information
    def save(self, commit=True):
        user = super().save(commit=commit)

        new_user = AppUsername(
            username=self.cleaned_data['username'],
            date=self.cleaned_data['date_of_birth'],
            user=user
        )

        if commit:
            new_user.save()
        return user


class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'details', 'category')
