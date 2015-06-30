# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
import sys

register = template.Library()


@register.filter(name='parity')
def parity(number):
    return True if number % 2 == 0 else False