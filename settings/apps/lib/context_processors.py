# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from datetime import datetime, timedelta
from gallerycolors.models import GalleryColors

from django.contrib.auth.forms import AuthenticationForm


def auth_form(request):
    out = {}
    
    out['auth_form'] = login_form = AuthenticationForm()

    if request.user.is_authenticated():
        out['auth_user'] = request.user
    
    return out


def gallerycolors(request):
    out = {}
    out['GalleryColors'] = GalleryColors.objects.all()[:10]
    return out