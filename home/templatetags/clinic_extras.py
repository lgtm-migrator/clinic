from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
	return field.as_widget(attrs={"class":css})

@register.filter(name='placeholder')
def addcss(field, text):
	return field.as_widget(attrs={"placeholder":text})