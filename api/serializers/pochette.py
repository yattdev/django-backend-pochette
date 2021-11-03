#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from gestion_prochette.models import Pochette


class PochetteSerializer(serializers.ModelSerializer):
    """ Serialize Pochette models from gestion_prochette """
    author = serializers.StringRelatedField()
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Pochette
        fields = (
            'id',
            'author',
            'title',
            'author_id',
            'image',
            'image_for_detail_page',
            'is_public',
            'slug',
        )
