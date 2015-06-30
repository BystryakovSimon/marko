from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import GalleryMixer, MixerImg


class MixerImg(admin.StackedInline):
    model = MixerImg
    extra = 6

class GalleryMixerAdmin(admin.ModelAdmin):
    model = GalleryMixer
    inlines = [MixerImg]
    search_fields = ['name']
    list_display = ('name','price','title', 'alt', 'img_small_preview',)

admin.site.register(GalleryMixer, GalleryMixerAdmin)