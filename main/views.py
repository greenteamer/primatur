# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from main.models import *
# Create your views here.

def home_view(request, template_name="main/home.html"):
    front_pages = Pages.objects.filter(is_aqua=True)

    #### test path settings
        # path = PROJECT_PATH
        # curputh = CURRPATH
        # media = MEDIA_ROOT
        # static = STATICFILES_DIRS
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))