from django import template
import numpy as np
import decimal

register = template.Library()

@register.filter
def convertDollar( quotient):
    return round( quotient/69, 2) # assuming the dollar rate to be 69

