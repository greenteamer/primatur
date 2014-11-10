# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import template
from django.contrib.flatpages.models import FlatPage
from django.template import context

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from slider.models import *


register = template.Library()


# @register.inclusion_tag("flexslider.html")
# def categories_tree(request):
# 	"""Возвращает дерево категорий"""
# 	return {'nodes': Category.objects.filter(is_active=True) }


def slider(context, request):
    slides = Slider.objects.all()
    return {
        # 'products': products,
        'slides': slides,
    }
register.inclusion_tag('slider/slider.html', takes_context=True)(slider)