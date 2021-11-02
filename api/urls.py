#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include

urlpatterns = [
    path('pochettes/', PochetteList.as_view(), name='pochette-list'),
    path('pochettes/<int:pk>/<slug:slug>', PochetteDetails.as_view(), name='pochette-details'),
    # third party apps urls
    path('auth', include('djoser.urls'), name="auth"),
    path('auth', include('djoser.urls.jwt')),
    #  path('auth', include('djoser.urls.authtoken'), name="auth_token"),
]
