from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import GalleryCountertops


class GalleryCountertopsAdmin(admin.ModelAdmin):
    list_display = ('title','alt', 'img_small_preview',)


admin.site.register(GalleryCountertops, GalleryCountertopsAdmin)