from django import template

register = template.Library()

@register.filter(name='format_date')
def format_date(date, value):
    return date.strftime(value)
