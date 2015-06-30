from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import GallerySink, SinkImg


class SinkImg(admin.StackedInline):
    model = SinkImg
    extra = 6

class GallerySinkAdmin(admin.ModelAdmin):
    model = GallerySink
    inlines = [SinkImg]
    search_fields = ['name']
    list_display = ('name','price','title', 'alt', 'img_small_preview',)

admin.site.register(GallerySink, GallerySinkAdmin)