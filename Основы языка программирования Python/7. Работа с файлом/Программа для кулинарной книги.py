# Вход:
        # Омлет
        # 3
        # Яйцо | 2 | шт
        # Молоко | 100 | мл
        # Помидор | 2 | шт

        # Утка по-пекински
        # 4
        # Утка | 1 | шт
        # Вода | 2 | л
        # Мед | 3 | ст.л
        # Соевый соус | 60 | мл

        # Запеченный картофель
        # 3
        # Картофель | 1 | кг
        # Чеснок | 3 | зубч
        # Сыр гауда | 100 | г

        # Фахитос
        # 5
        # Говядина | 500 | г
        # Перец сладкий | 1 | шт
        # Лаваш | 2 | шт
        # Винный уксус | 1 | ст.л
        # Помидор | 2 | шт

# Выход: 
          # cook_book = {
          #   'Омлет': [
          #     {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
          #     {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
          #     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
          #     ],
          #   'Утка по-пекински': [
          #     {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
          #     {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
          #     {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
          #     {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
          #     ],
          #   'Запеченный картофель': [
          #     {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
          #     {'ingridient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
          #     {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
          #     ]
          #   }

with open('Список рецептов.txt') as f:
  cook_book = {}
  ingredients_dict = {}
  while True:
    ingredient_list = []
    food = f.readline().strip()
    if not food:
      break
    for i in range(int(f.readline().strip())):
      ingredient = f.readline().strip().split('|')
      ingredient_list.append({'ingridient_name':ingredient[0],'quantity':ingredient[1],'measure':ingredient[2]})
    f.readline().strip()
    cook_book[food] = ingredient_list
print(cook_book)

# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить:
# Вход: get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Выход:  {
        # 'Картофель': {'measure': 'кг', 'quantity': 2},
        # 'Молоко': {'measure': 'мл', 'quantity': 200},
        # 'Помидор': {'measure': 'шт', 'quantity': 4},
        # 'Сыр гауда': {'measure': 'г', 'quantity': 200},
        # 'Яйцо': {'measure': 'шт', 'quantity': 4},
        # 'Чеснок': {'measure': 'зубч', 'quantity': 6}
        # }

def get_shop_list_by_dishes (dishes, person_count):
  all_ingridients_dict = {}

  for dish in dishes:
    for ingridient in cook_book[dish]:
      ingridients_dict = {}
      one_ingridient = ingridient['ingridient_name']
      ingridients_dict['measure'] = ingridient['measure']
      ingridients_dict['quantity'] = int(ingridient['quantity']) * person_count
      all_ingridients_dict[one_ingridient] = ingridients_dict
  print(all_ingridients_dict)

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)



