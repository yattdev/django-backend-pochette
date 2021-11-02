#!/usr/bin/env python
# -*- coding: utf-8 -*-

from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

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
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            password=make_password(validated_data['password']),
        )
        return user.save()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'role',
        )

