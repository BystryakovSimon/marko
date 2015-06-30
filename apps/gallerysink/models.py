# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin

class GallerySink(models.Model):
    name      = models.CharField('Модель', max_length=50)
    price     = models.IntegerField('Цена', blank=True)
    title     = models.TextField('Описание', blank=True)
    alt       = models.CharField('alt картинки', max_length=50, blank=True)
    img_small = models.ImageField('Картинка (миниатюра)',     upload_to="images/gallerysink/small/")
    img_full  = models.ImageField('Картинка (полный размер)', upload_to="images/gallerysink/full/")

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
        verbose_name        = 'Мойка'
        verbose_name_plural = 'Галерея моек'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return self.name

class SinkImg(models.Model):
    gallerysink = models.ForeignKey(GallerySink, related_name="get_images")
    alt         = models.CharField('alt картинки', max_length=50, blank=True)
    img_small   = models.ImageField('Картинка (миниатюра)',     upload_to="images/gallerysink/img/small/")
    img_full    = models.ImageField('Картинка (полный размер)', upload_to="images/gallerysink/img/full/")    

    class Meta:
        verbose_name        = 'Мойка'
        verbose_name_plural = 'Галерея'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return self.alt

class GallerySinkPlugin(CMSPlugin):
    gallerysink = models.ForeignKey(GallerySink)
