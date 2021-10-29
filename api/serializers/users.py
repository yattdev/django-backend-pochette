#!/usr/bin/env python
# -*- coding: utf-8 -*-

from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    """ Override djoser's user registration serializers"""
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )

class UserSerializer(UserSerializer):
    """ Override user details serializers"""
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'role',
        )
