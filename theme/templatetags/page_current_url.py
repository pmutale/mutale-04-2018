from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def page_current_url(value):
    return mark_safe(value.split('/')[2])

