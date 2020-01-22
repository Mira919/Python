# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. 
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;

# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;

# объединить все дублирующиеся записи о человеке в одну.

# Записать получившийся список в файл

from pprint import pprint
import re
import csv

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# делает нормальный формат для ФИО
def format_name(contacts_list):
    format_name_list = []
    pattern = re.compile(r'^([А-Яа-я]+)[\s|,]([А-Яа-я]+)[\s|,]([А-Яа-я]+|)')
    replacer = r'\1, \2, \3'
    for people in contacts_list:
        people = ','.join(people) # список в строку
        result = [pattern.sub(replacer, people)] # форматирование
        format_name_list.append(result)
    return format_name_list

# делает нормальный формат для телефонов
def format_telephone(contacts_list):
    format_telephone_list = []
    pattern = re.compile(r'(\+7|7|8)[\s\(]*(\d{3})[\)\s]*(\d+)-?(\d+)-?(\d+)([\s\(]*доб.\s\d{1,4}\)?)?')
    replacer = r'+7(\2)\3-\4-\5 \6'
    for people in contacts_list:
        people = ','.join(people) # список в строку
        result = [pattern.sub(replacer, people)] # форматирование
        format_telephone_list.append(result)
    return format_telephone_list

format_name_telephone_list = format_telephone(format_name(contacts_list))

# удаляет повторяющиеся контакты
def del_duplicates(contacts_list):
    new_list_contact = []
    for contact in contacts_list: # выводим каждый контакт в списке
        contact = ' '.join(contact) # каждый контакт из списка в строку
        contact = contact.split(',') # каждую строку в список, разделяя слова через пробел (чтобы можно было разделить Имя, Фамилию и тд.Иначально каждый список контактов имя по 1 элементу)
        new_list_contact.append(contact) # список из списков контактов

    for contact in new_list_contact: # удалить пустые и ненужные элементы списка
        while contact[3] == '':
            del(contact[3])

    name_list = []
    set_list_contact = []
    for contact in new_list_contact: # выводим каждый контакт в списке
        if contact[0] not in name_list: # если имя контакта не в списке name_list, то...
            name_list.append(contact[0]) # ...добавляем имя контакта туда
            set_list_contact.append(contact) # ...добавляем сам контакт в список set_list_contact
    return set_list_contact

contacts_list = del_duplicates(format_name_telephone_list)

# записываем в файл csv
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
pprint(contacts_list)
