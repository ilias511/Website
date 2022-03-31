from django import test as django_test

from sites.models import AppUsername


class AppUsernameTest(django_test.TestCase):

    def test_true(self):
        self.assertTrue(True)

    # def test_user_create_when_everything_is_valid(self):
    #     user = AppUsername(username='Youngtask' ,age=14)
    #     user.save()
    #     self.assertIsNotNone(user.pk)

