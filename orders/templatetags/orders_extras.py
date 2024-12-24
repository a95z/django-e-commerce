from django import template

register = template.Library()


@register.filter()
def split(str, args):
    return str.split(args.split(",")[0])[int(args.split(",")[1])]
