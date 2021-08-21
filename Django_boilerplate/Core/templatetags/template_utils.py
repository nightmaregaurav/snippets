from django import template
from django.template.loader import get_template

register = template.Library()


@register.filter()
def template_exists(value1):
    try:
        _ = get_template(value1)
        return True
    except template.TemplateDoesNotExist:
        return False
