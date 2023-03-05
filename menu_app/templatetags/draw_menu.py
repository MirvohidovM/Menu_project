from django import template

register = template.Library()

from menu_app.models import Menu


@register.simple_tag
def any_function():
    return Menu.objects.all()