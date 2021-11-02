from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.test import APIClient

User = get_user_model() # Get user models

class UserAccountTestCase(TestCase):
    """ TestCase for UserAccount models"""
    @classmethod
    def setUpTestData(cls):

        # Create test user
        cls.user_test = User.objects.create(
            email='user_test@gmail.com',
            password=make_password('test_user123'),
        )
        cls.user_test.save()

       # Create super user
       cls.test_admin = User.objects.create_superuser(email='admin@gmail.com',
                                                      password='test_admin123')
       cls.test_admin.save()

    def test_create_user(self):
        user = User.objects.get(id=1)
        self.assertEqual(f'{user.email}', f'{self.user_test.email}')
        self.assertTrue(user.check_password('test_user123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superUser = User.objects.get(email='admin@gmail.com')
        self.assertTrue(superUser.check_password('test_admin123'))
        self.assertTrue(superUser.is_superuser)
        self.assertTrue(superUser.is_active)
        self.assertTrue(superUser.is_staff)

    def test_login_user(self):
        client = APIClient()

