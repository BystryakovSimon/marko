from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import GalleryColors


class GalleryColorsAdmin(admin.ModelAdmin):
    list_display = ('number','name','title', 'alt', 'img_small_preview',)


admin.site.register(GalleryColors, GalleryColorsAdmin)