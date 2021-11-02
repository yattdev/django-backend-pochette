from django.contrib import admin
from .models import Pochette

class PochetteAdmin(admin.ModelAdmin):
    """ Custom pochette model for admin dashboard """
    list_display = ('title', 'author', 'pub_date', 'is_public')
    list_filter = ('pub_date', 'author')


admin.site.register(Pochette, PochetteAdmin) # add Pochette models to admin
