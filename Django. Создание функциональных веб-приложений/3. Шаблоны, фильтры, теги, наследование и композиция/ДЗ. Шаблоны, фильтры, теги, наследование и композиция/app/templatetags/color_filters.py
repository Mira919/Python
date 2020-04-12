from django import template # фильтр

register = template.Library() # фильтр


@register.filter # фильтр
def color_value(value): # фильтр цветов, если значение поля < 0 то цвет поля булет зеленый и так далее
    color = 'white'

    if value:
        value = float(value)
        if value < 0:
            color = 'green'
        elif 1 < value < 2:
            color = '#F78181'
        elif 2 < value < 5:
            color = '#FE2E2E'
        elif 5 < value:
            color = '#B40404'
    else:
        pass
    return color
