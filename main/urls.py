# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    # Главная страница
    url(r'^$', 'home_view',
        {'template_name':'main/home.html'},
        name='home'),
    # Просмотр товара
    # url(r'^product/(?P<product_slug>[-\w]+)/$', 'product_view',
    #     {'template_name':'catalog/product.html'},
    #     name='catalog_product'),
)
