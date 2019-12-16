import csv

flats_list = list()

with open('Квартиры.csv', newline='', encoding='utf-8') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

header = flats_list.pop(0) # Вырезать первый список
# Цикл, который проходит по всем квартирам, и показывает только новостройки и их порядковые номера в файле и подсчет количества новостроек.
new_built = 0
for flat in flats_list:
    if "новостройка" in flat:
        print(flat[0], flat[2])
        new_built += 1
print("Всего новостроек:", new_built)

# Описание квартиры в виде словаря: ID, Количество комнат;Новостройка/вторичка, Цена (руб).
flat_all = []
for flat in flats_list:
    flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
    flat_all.append(flat_info)
print(flat_all)

# Выводит метро и квартиры у него, чтобы значением словаря были:"id", "rooms", "type", "price".
subway_dict = {}
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append({"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]})
print(subway_dict)

# Подсчитывает и выводит, сколько квартир нашлось у каждого метро.
for subway, subway2 in subway_dict.items():
  if subway == "":
    subway = "Неизвестное метро"
  print("У", subway,"нашлось", len(subway2), "квартир(ы)")

