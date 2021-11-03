#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import BytesIO

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.files import File
from django.test import TestCase
from django.urls import reverse_lazy
from PIL import Image
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from gestion_prochette.models import Pochette


class PochetteEndpointsTestCase(TestCase):
    """ Test pochette endpoints """

    @classmethod
    def setUpTestData(cls):
        #  TemporaryUploadedFile return tuple content firstly ou tmp img
        album_photo = Image.new('RGB', (60, 30), color='red')
        io = BytesIO()
        album_photo.save(io, 'JPEG')
        cls.img = File(io)

        # Create a test user
        cls.user = get_user_model().objects.create(
            email="test_user@gexample.com",
            password=make_password('password_123')
        )
        cls.user.save()

    @classmethod
    def setUp(cls):
        token = RefreshToken.for_user(user=cls.user)
        cls.clientApi = APIClient()
        cls.clientApi.credentials(HTTP_AUTHORIZATION='Bearer ' + f'{token.access_token}')

        # Create a pochette test
        cls.p_test = Pochette.objects.create(
            title='test pochette title',
            is_public=True,
            image=cls.img,
            author=cls.user
        )
        cls.p_test.save()

    def test_pochette_list(self):
        response = self.clientApi.get(reverse_lazy('pochette-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pochette_create(self):
        data = {
            'title': 'test pochette title',
            'is_public': True,
            'image': self.img,
            'author': self.user
        }
        response = self.clientApi.post(reverse_lazy('pochette-list'), data)
        #  TODO: handle fileImage later
        #  self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pochette_details(self):
        response = self.clientApi.get(
            reverse_lazy('pochette-details', kwargs={
                'pk': self.p_test.id,
                'slug': self.p_test.slug}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pochette_details(self):
        response = self.clientApi.delete(
            reverse_lazy('pochette-details', kwargs={
                'pk': self.p_test.id,
                'slug': self.p_test.slug}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

