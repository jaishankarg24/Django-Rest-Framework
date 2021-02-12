from django import template


register=template.Library()

def slicing1(value):
	result=value[0:2]
	return result

def slicing2(value, n):
	result=value[0:n]
	return result


register.filter('slicing1', slicing1)
register.filter('slicing2', slicing2)