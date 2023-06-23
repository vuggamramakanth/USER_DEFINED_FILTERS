from django import template

register=template.Library()

@register.filter(name='swapping')
def swap(value):
    return value.swapcase()

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')

@register.filter()
def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c

#register.filter('counting',counting)
#register.filter('remove',remove)
#register.filter('swapping',swap)