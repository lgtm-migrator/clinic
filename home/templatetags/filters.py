from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    temp = dictionary.get(key)
    if (key=="book" or key == "available") and temp == None:
        return 0
    return temp
