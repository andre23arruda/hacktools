from django import template

register = template.Library()

@register.filter(name='get_value_of_index')
def get_value_of_index(value, index):
    value = eval(value)
    return value[index]
