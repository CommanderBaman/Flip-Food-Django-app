from django import template

register = template.Library()

@register.filter
def convertDollar( quotient):
    return quotient/69

