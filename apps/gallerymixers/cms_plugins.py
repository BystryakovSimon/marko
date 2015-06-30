# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GalleryMixer, GalleryMixerPlugin, MixerImg
from django.utils.translation import ugettext as _

class CMSGalleryMixerPlugin(CMSPluginBase):
    name = _(u"Галерея смесителей")
    render_template = "gallerymixers.html"

    def render(self, context, instance, placeholder):

        context.update({
            'gallerymixer'     : GalleryMixer.objects.all().order_by("-id")[:10],
            'lastgallerymixer' : GalleryMixer.objects.all().order_by("-id")[0],
            'object'           : instance,
            'placeholder'      : placeholder
        })
        return context

plugin_pool.register_plugin(CMSGalleryMixerPlugin)