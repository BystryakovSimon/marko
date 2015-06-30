# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GallerySink, GallerySinkPlugin, SinkImg
from django.utils.translation import ugettext as _

class CMSGallerySinkPlugin(CMSPluginBase):
#    model = GalleryColorsPlugin
    name = _(u"Галерея моек")
    render_template = "gallerysink.html"

    def render(self, context, instance, placeholder):

        context.update({
#            'gallerycolors' : instance.gallerycolors,
            'gallerysink'     : GallerySink.objects.all().order_by("-id")[:10],
            'lastgallerysink' : GallerySink.objects.all().order_by("-id")[0],
            'object'          : instance,
            'placeholder'     : placeholder
        })
        return context

plugin_pool.register_plugin(CMSGallerySinkPlugin)