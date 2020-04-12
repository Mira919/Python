from django import template

register = template.Library()


@register.filter
def camel_string(s): # фильтр делает: апельсин -> аПеЛьСиН
    return ''.join([c.lower() if idx % 2 == 0 else c.upper() for idx, c in enumerate(s)])