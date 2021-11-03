from io import BytesIO

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.files import File
from django.test import TestCase
from PIL import Image

from gestion_prochette.models import Pochette


class PochetteTestCase(TestCase):
    """ TestCase for Pochette models """
    @classmethod
    def setUpTestData(cls):
        # Creat author test
        cls.author_test = get_user_model().objects.create(
            email="author_test@gmail.com",
            password=make_password('password_123'))
        cls.author_test.save()

        #  TemporaryUploadedFile return tuple content firstly ou tmp img
        album_photo = Image.new('RGB', (60, 30), color='red')
        cls.io = BytesIO()
        album_photo.save(cls.io, 'JPEG')
        # Create pochette test
        #  cls.album_photo = TemporaryUploadedFile('photo_music_ablum.jpg',
        #  io,
        #  size=1,
        #  charset='utf8'),
        cls.pochette_test = Pochette.objects.create(
            title="The fantastic music",
            image=File(cls.io),
            author=cls.author_test,
            is_public=True,
            slug="The-fantastic-music-slug-de-test",
        )
        cls.pochette_test.save()

    def test_pochette_content(self):
        pochette = Pochette.objects.get(author=self.author_test)

        self.assertEqual(f'{pochette.title}', f'{self.pochette_test.title}')
        self.assertEqual(f'{pochette.slug}', f'{self.pochette_test.slug}')
        self.assertTrue(pochette.is_public)
        self.assertEqual(f'{pochette.author.email}',
                         f'{self.author_test.email}')
        #  self.assertEqual('photo_music_ablum.jpg',
        #  f'{self.album_photo.filename}')
