from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient

User = get_user_model() # Get user models

class UserAccountTestCase(TestCase):
    """ TestCase for UserAccount models"""
    @classmethod
    def setUpTestData(cls):

       # Create test user
       cls.test_user = User.objects.create(email='test_user@gmail.com',
                                       password=('test_user123'))
       cls.test_user.save()

       # Create super user
       cls.test_admin = User.objects.create_superuser(email='admin@gmail.com',
                                                      password='test_admin123')
       cls.test_admin.save()

    def test_create_user(self):
        user = User.objects.get(id=1)
        self.assertEqual(f'{user.email}', f'{self.test_user.email}')
        self.assertEqual(f'{user.password}', f'{self.test_user.password}')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superUser = User.objects.get(email='admin@gmail.com')
        self.assertEqual(f'{superUser.password}', f'{self.test_admin.password}')
        self.assertTrue(superUser.is_superuser)
        self.assertTrue(superUser.is_active)
        self.assertTrue(superUser.is_staff)

    def test_login_user(self):
        client = APIClient()

       
