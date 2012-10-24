from django import template

register = template.Library()

@register.filter   
def subtract(value, arg):
	print value
	print arg
	print value - int(arg)
	return value - int(arg)
