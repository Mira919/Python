import vk
import time
import datetime
import json
import random
from pymongo import MongoClient

access_token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
v = '5.103'

session = vk.Session(access_token)
api = vk.API(session, v=v)

# получаем страницу пользователя, которому надо найти пару
def get_user(id):
    user = api.users.get(user_ids = id, fields = 'bdate,sex,city,interests')
    groups = api.users.getSubscriptions(user_id=id, extended = 1)
    for i in user:
       i['groups'] = groups
    return user

# получаем список из страниц пользователей, из которых будем выбирать пару. (Страницы с id от 1 до 100)
def get_users():
    users_id = []
    for i in range(10):
        users_id.append(random.randrange(1, 169989152))
    users_id.append('91098303')

    users_list = []
    for user_id in users_id:
        user = api.users.get(user_ids = user_id, fields = 'bdate,sex,city,interests')
        time.sleep(3)
        if 'deactivated' not in user[0]: # не берем пользователя если он удален
            if user[0]['is_closed'] == False: # не берем если у пользователя закрыта страница
                groups = api.users.getSubscriptions(user_id=user_id, extended=1)
                for i in user:
                    i['groups'] = groups
                users_list.append(user)
    return users_list

def get_couple(): # ищем пару по критериям
    user = get_user('169989152')
    users = get_users()
    couple = []

    for people in users:
        if user[0]['sex'] != people[0]['sex'] and user[0]['sex'] != 0: # проверка по полу
            if 'city' in people[0] and user[0]['city']['title'] == people[0]['city']['title']: # проверка по городу
                try:
                    age_user = str((datetime.datetime.today() - datetime.datetime.strptime(user[0]['bdate'], '%d.%m.%Y')) / 365)[:2]
                    age_people = str((datetime.datetime.today() - datetime.datetime.strptime(people[0]['bdate'], '%d.%m.%Y'))/365)[:2]
                except:
                    pass
                if int(age_user) - int(age_people) < 5 and int(age_user) - int(age_people) > -5: # проверка по возрасту (+- 5 лет)
                    couple.append(people)
    return couple

# сохранить данные в файл JSON
with open('couple.json', 'w', encoding='utf-8') as file:
    json.dump(get_couple(), file, ensure_ascii=False, indent=2)
# with open('couple.json', encoding = 'utf-8-sig' ) as file:
#      data = json.load(file)
# for user in data:
#     print(user[0])

# сохранить данные в БД MongoDB
client = MongoClient()
my_db = client['vk_api'] # создать/обратится к бд
couple = my_db['couple'] # создать/обратится к коллекции
for list in get_couple():
    for people in list:
        couple.insert_one(people)
print(list(couple.find())) # проверка

