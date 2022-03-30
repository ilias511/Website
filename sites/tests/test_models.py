from django.test import TestCase

from sites.models import AppUsername


class AppUsernameTest(TestCase):
    def test_user_create_when_everything_is_valid(self):
        user = AppUsername(username='Youngtask',age=14)
        user.save()
        self.assertIsNotNone(user.pk)


