from django import template


register=template.Library()

@register.filter(name='slicing1')
def slicing1(value):
	result=value[0:3]
	return result

@register.filter(name='slicing2')
def slicing2(value, n):
	result=value[0:n]
	return result


#register.filter('slicing1', slicing1)
#register.filter('slicing2', slicing2)