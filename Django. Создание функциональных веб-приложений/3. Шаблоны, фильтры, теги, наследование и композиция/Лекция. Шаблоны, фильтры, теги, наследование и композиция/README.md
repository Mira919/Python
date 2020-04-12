
# Шаблоны, фильтры, теги, наследование и композиция

## Шаблоны (HTML странички)

app/templates/card.html
app/templates/user_info.html

## Теги {} (Python код в шаблоне HTML)

app/templates/user_info.html

## Фильтры {} (Применяются к любой переменной, например чтобы что первая буква слова всегда была большая)

app/templatetags/string_filters

## Наследование (вставляем весь код в блоке в каой либо файл)

app/templates/user_info.html
templates/base.html

## Композиция (вставляет в это место код из какого - либо файла)

app/templates/card.html
app/templates/user_info.html
