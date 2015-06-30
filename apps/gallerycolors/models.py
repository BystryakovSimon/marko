# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin

class GalleryColors(models.Model):
    number    = models.IntegerField('Номер')
    name      = models.CharField('Название', max_length=50)
    title     = models.CharField('Описание картинки', max_length=50, blank=True)
    alt       = models.CharField('alt картинки', max_length=50, blank=True)
    img_small = models.ImageField('Картинка (миниатюра)',     upload_to="images/gallerycolors/small/")
    img_full  = models.ImageField('Картинка (полный размер)', upload_to="images/gallerycolors/full/")

    def img_small_preview(self):
        if self.img_small:
            return u'<img src="%s" width="100" >' % self.img_small.url
        else:
            return '(none)'
    img_small_preview.short_description = u'Миниатюра'
    img_small_preview.allow_tags        = True
    
    def img_full_preview(self):
        if self.img_full:
            return u'< img src="%s" width="100"/>' % self.img_full.url
        else:
            return '(none)'
    img_full_preview.short_description = u'Миниатюра'
    img_full_preview.allow_tags        = True
    
    class Meta:
        verbose_name        = 'Цавет'
        verbose_name_plural = 'Галерея цветов'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return self.name

class GalleryColorsPlugin(CMSPlugin):
    gallerycolors = models.ForeignKey(GalleryColors)
