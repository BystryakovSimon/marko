# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GalleryCountertops, GalleryCountertopsPlugin
from django.utils.translation import ugettext as _

class CMSGalleryCountertopsPlugin(CMSPluginBase):
#    model = GalleryCountertopsPlugin
    name = _(u"Галерея столешниц")
    render_template = "gallerycountertops.html"

    def render(self, context, instance, placeholder):

        context.update({
#            'gallerycountertops' : instance.gallerycountertops,
            'lastcountertops'    : GalleryCountertops.objects.all().order_by("-id")[:10],
            'object'             : instance,
            'placeholder'        : placeholder
        })
        return context

plugin_pool.register_plugin(CMSGalleryCountertopsPlugin)