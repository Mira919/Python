import csv
import re
from pymongo import MongoClient

# Загрузить данные в бд из CSV-файла. Прочитать файл с данными и записать в коллекцию
def read_data(csv_file, collection):
    with open(csv_file, encoding='utf8') as csvfile:
        rows_list = list() # создать список
        reader = csv.DictReader(csvfile) # записать данные CSV файла в reader

        for row in reader: # берет каждую строчку
            row = dict(row) # преобразует в словарь
            row['Цена'] = int(row['Цена'])
            rows_list.append(row)
        collection.insert_many(rows_list) # вставляет список из словарей в Mongo

# Отсортировать билеты из базы по возрастанию цены
def find_cheapest(collection):
    sorted_list = collection.find().sort('Цена', 1) # сортировка поля ЦЕНА по возрастанию и выводит полные документы. 0 – убыв, 1 – возр
    print(list(sorted_list))

# Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"), и вернуть их по возрастанию цены
def find_by_name(name, collection):
    regex = re.compile(name, re.I ) # строка по которой надо искать, игнорирует регистр символов
    sorted_list = collection.find({'Исполнитель': regex}).sort('Цена', 1) # Список. Ищет в коллекции tickets_collection по полю ИСПОЛНИТЕЛЬ и сортировать по полю ЦЕНА, по возрастанию (0 – убыв, 1 – возр)
    for item in sorted_list:
        print(item)

if __name__ == '__main__':
    client = MongoClient()
    mongo_db = client['test_db']  # получаем БД
    tickets_collection = mongo_db['tickets']  # создать или обратится к коллекции tickets

    read_data('artists.csv', tickets_collection)
    find_cheapest(tickets_collection)
    find_by_name('T', tickets_collection)