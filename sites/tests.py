from django import test as django_test
from django.urls import reverse

from sites.models import AppUsername, Post, AppUser


#
# class AppUsernameTest(django_test.TestCase):
#
#     def test_true(self):
#         self.assertTrue(True)
#
#     # def test_user_create_when_everything_is_valid(self):
#     #     user = AppUsername(username='Youngtask' ,age=14)
#     #     user.save()
#     #     self.assertIsNotNone(user.pk)


class TestViews(django_test.TestCase):

    def test_project_home(self):
        client = django_test.Client()

        response = client.get(reverse('home'))


        self.assertEquals(response.status_code,200)
        # self.assertTemplateUsed(response,'base/base.html')
        self.assertTemplateUsed(response,'home.html')

    def test_project_home_page_with_posts(self):
        client = django_test.Client()

        user = AppUser.objects.create(
                email='ilias.task@gmail.com',
                is_staff=False,
                is_superuser=False

            )
        p = Post.objects.create(
            title='random',
            details='random 2 test',
            category='Crypto',
            user = user

        )
        p.save()

        response = client.get(reverse('home'))

        posts = response.context['post']

        for p in posts:
            self.assertIsNotNone(p)
