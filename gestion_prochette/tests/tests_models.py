from django.test import TestCase
from gestion_prochette.models import Pochette
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.files.uploadedfile import TemporaryUploadedFile
from os.path import exists
from pathlib import Path


class PochetteTestCase(TestCase):
    """ TestCase for Pochette models """
    @classmethod
    def setUpTestData(cls):
        # Creat author test
        cls.author_test = get_user_model().objects.create(
            email="author_test@gmail.com",
            password=make_password('password_123')
        )
        cls.author_test.save()

        album_photo = TemporaryUploadedFile('photo_music_ablum.jpg',
                                            b'Whatever content',
                                            size=1,
                                            charset='utf8'),
        #  TemporaryUploadedFile return tuple content firstly ou tmp img
        cls.album_photo = album_photo[0]
        # Create pochette test
        cls.pochette_test = Pochette.objects.create(
            title="The fantastic music",
            image=cls.album_photo,
            author=cls.author_test,
            is_public=True,
            slug="The-fantastic-music-slug-de-test",
        )
        cls.pochette_test.save()

    def test_pochette_content(self):
        pochette = Pochette.objects.get(id=1)
        
        self.assertEqual(f'{pochette.title}', f'{self.pochette_test.title}') 
        self.assertEqual(f'{pochette.slug}', f'{self.pochette_test.slug}') 
        self.assertTrue(pochette.is_public) 
        self.assertEqual(f'{pochette.author.email}',
                         f'{self.author_test.email}')
        self.assertEqual('photo_music_ablum.jpg', f'{self.album_photo}')
