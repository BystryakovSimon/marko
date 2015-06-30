# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GalleryColors, GalleryColorsPlugin
from django.utils.translation import ugettext as _

class CMSGalleryColorsPlugin(CMSPluginBase):
#    model = GalleryColorsPlugin
    name = _(u"Галерея цветов")
    render_template = "gallerycolors.html"

    def render(self, context, instance, placeholder):

        context.update({
#            'gallerycolors' : instance.gallerycolors,
            'lastcolors'    : GalleryColors.objects.all().order_by("-id")[:10],
            'object'        : instance,
            'placeholder'   : placeholder
        })
        return context

plugin_pool.register_plugin(CMSGalleryColorsPlugin)