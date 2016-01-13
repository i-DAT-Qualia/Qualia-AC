from django import template
from django.template import RequestContext
from django.template.defaultfilters import stringfilter
from django.conf import settings

register = template.Library()

@register.inclusion_tag('components/c3/includes.html')
def c3_includes():
    return {
        'STATIC_URL': settings.STATIC_URL
    }

@register.inclusion_tag('components/c3/bar.html')
def c3_bar_html(name, title):
    return {
        'name': name,
        'title': title,
        'STATIC_URL': settings.STATIC_URL
    }

@register.inclusion_tag('components/c3/bar.js')
def c3_bar_js(name, data_url, y_label):
    return {
        'name': name,
        'data_url': data_url,
        'y_label': y_label
    }

@register.inclusion_tag('components/c3/pie.html')
def c3_pie_html(name, title):
    return {
        'name': name,
        'title': title,
        'STATIC_URL': settings.STATIC_URL
    }

@register.inclusion_tag('components/c3/pie.js')
def c3_pie_js(name, data_url, y_label):
    return {
        'name': name,
        'data_url': data_url,
        'y_label': y_label
    }
