# Generated by Django 3.2.9 on 2021-11-03 02:04

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_prochette', '0009_alter_pochette_image_for_detail_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pochette',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], force_format=None, keep_meta=True, quality=75, size=[550, 350], upload_to='albums_photo/'),
        ),
        migrations.AlterField(
            model_name='pochette',
            name='image_for_detail_page',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left'], editable=False, force_format=None, keep_meta=True, quality=75, size=[400, 240], upload_to='albums_photo_details/'),
        ),
    ]
