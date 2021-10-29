#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include

urlpatterns = [
    # User auth endpoints
    path('auth', include('djoser.urls')),
    path('auth', include('djoser.urls.jwt')),
]
