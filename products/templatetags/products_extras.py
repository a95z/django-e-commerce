from django import template

register = template.Library()


@register.filter(name="range")
def range_f(num):
    return range(num)
