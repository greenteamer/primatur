# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class Pages(models.Model):
    name = models.CharField(verbose_name=u'Название страницы', max_length=100)
    slug = AutoSlugField(editable=True)
    image = models.ImageField(verbose_name=u'Изображение', upload_to='pages')

    body = RichTextField()
    is_aqua = models.BooleanField(verbose_name=u'На главную', default=False)

    def __unicode__(self):
        return self.name

    def page_is_main(self):
        return self.is_aqua

class Block(models.Model):
    text = RichTextField()
    is_main = models.BooleanField(verbose_name=u'Блок рядом со слайдером', default=False)

    def block_is_main(self):
        return self.is_main
