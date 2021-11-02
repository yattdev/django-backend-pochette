from django.db.models import (CharField,
                              DateField,
                              ForeignKey,
                              ImageField,
                              Model,
                              CASCADE,
                              BooleanField,
                              )
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField

class Pochette(Model):
    """ Models for music album covers """
    title = CharField(verbose_name="titre",
                             unique=True,
                             blank=False,
                             max_length=45)
    image = ResizedImageField(
        size=[400, 240],
        crop=['top', 'left'],
        upload_to='albums_photo/'
    )
    image_for_detail_page = ResizedImageField(
        size=[550, 350],
        editable=False,
        upload_to='albums_photo_details/',
        blank=True,
    )
    pub_date = DateField(auto_now_add=True)
    author = ForeignKey(get_user_model(),
                               on_delete=CASCADE,
                               related_name="pochettes")
    slug = AutoSlugField(populate_from='title',
                         unique_with=['title', 'pub_date__month'],
                         editable=True,
                         blank=True,
                         )
    is_public = BooleanField(verbose_name='public', default=False)

    def save(self, *args, **kwargs):
        if self.image:
            self.image_for_detail_page = self.image
        super().save(*args, **kwargs)
