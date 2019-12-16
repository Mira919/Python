# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях (файл newsafr.xml) слов длиннее 6 символов.


from pprint import pprint

import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
root = tree.getroot()
items = root.findall('channel/item')

# Все слова в список и разделены запятой
news = []
for item in items:
    new = item.find('description').text
    news = news + new.split(" ")

# все слова в нижнем регистре
word_lower = []
for words in news:
    word_lower.append(words.lower())

# Cловарь, ключ - сколько раз это слово повторяется, значение - слово из слова, которые длинее 6 букв
word_list = {}
for words in word_lower:
    if len(words) > 6:
        w = word_lower.count(words)
        word_list.setdefault(w, set())  # чтобы в словаре можно было применять add
        word_list[w].add(words)  # чтобы в словаре можно было применять add

str = ''
for word_count in sorted(word_list.keys(), reverse=True): # сортировка ключей в словаре
    str = str + ' '.join(word_list[word_count]) + ' '  # преобразовать множества в строку
for word in str.split(' ')[:10]:
    print(f"Слово '{word}' повторилось {word_lower.count(word)} раз(а)")
    
    
# Слово 'туристов' повторилось 40 раз(а)
# Слово 'компании' повторилось 27 раз(а)
# Слово 'wilderness' повторилось 23 раз(а)
# Слово 'странах' повторилось 21 раз(а)
# Слово 'туризма' повторилось 19 раз(а)
# Слово 'туристы' повторилось 17 раз(а)
# Слово 'которые' повторилось 16 раз(а)
# Слово 'африканских' повторилось 16 раз(а)
# Слово 'носорогов' повторилось 14 раз(а)
# Слово 'является' повторилось 14 раз(а)
