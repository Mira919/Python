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


def get_user(id): # получаем страницу пользователя, которому надо найти пару
    start_time = datetime.datetime.now()
    user = api.users.get(user_ids=id, fields='bdate,sex,city,interests')
    groups = api.users.getSubscriptions(user_id=id, extended=1)
    time.sleep(1.5)
    for i in user:
        i['groups'] = groups
    print(f'Функция get_user исполнялась {datetime.datetime.now() - start_time}')
    return user


def get_users(): # получаем список из страниц пользователей, из которых будем выбирать пару. (Страницы с id от 1 до 100)
    start_time = datetime.datetime.now()
    users_id = []
    for i in range(1):
        users_id.append(random.randrange(1, 169989152))
    users_id += ['91098303', '162441244', '76956315', '143426463', '146586509', '151363555', '158366434', '161726777', '162764029', '56862127']

    users_list = []
    for user_id in users_id:
        user = api.users.get(user_ids = user_id, fields='bdate,sex,city,interests, domain')
        time.sleep(2)
        if 'deactivated' not in user[0]: # не берем пользователя если он удален
            if not user[0]['is_closed']: # не берем если у пользователя закрыта страница
                groups = api.users.getSubscriptions(user_id=user_id, extended=1)
                for i in user:
                    i['groups'] = groups
                users_list.append(user)
    print(f'Функция get_users исполнялась {datetime.datetime.now() - start_time}')
    return users_list


def get_couple(): # ищем пару по критериям
    start_time = datetime.datetime.now()
    user = get_user('169989152')
    users = get_users()
    couple = []

    for people in users:
        if user[0]['sex'] != people[0]['sex'] and user[0]['sex'] != 0: # проверка по полу
            if 'city' in people[0] and user[0]['city']['title'] == people[0]['city']['title']: # проверка по городу
                try:
                    age_user = str((datetime.datetime.today() - datetime.datetime.strptime(user[0]['bdate'], '%d.%m.%Y')) / 365)[:2]
                    age_people = str((datetime.datetime.today() - datetime.datetime.strptime(people[0]['bdate'], '%d.%m.%Y'))/365)[:2]
                    if 5 > int(age_user) - int(age_people) > -5:  # проверка по возрасту (+- 5 лет)
                        couple.append(people)
                except:
                    pass
    print(f'Функция get_couple исполнялась {datetime.datetime.now() - start_time}')
    return couple


def get_url_photo():
    start_time = datetime.datetime.now()
    list_to_save = []
    for simple_list in get_couple():
        for user in simple_list:
            top3_like = []
            user_photo = api.photos.get(owner_id = user['id'], album_id = 'profile', extended = 1)
            time.sleep(2)
            for photo in user_photo['items']:
                top3_like.append(photo['likes']['count'])
            top3_like.sort(reverse=True)

        url_list = []
        top_dict = {}
        for user in simple_list:
            user_photo = api.photos.get(owner_id=user['id'], album_id='profile', extended=1)
            for photo in user_photo['items']:
                if photo['likes']['count'] in top3_like[:3]:
                    url_list.append(photo['sizes'][0]['url'])
            top_dict['id'] = 'https://vk.com/' + user['domain']
            top_dict['photos'] = url_list[:3]
            list_to_save.append(top_dict)
    print(f'Функция get_photo исполнялась {datetime.datetime.now() - start_time}')
    return list_to_save


func = get_url_photo()


def save_to_file(file_name): # сохранить данные в файл JSON
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(func, file, ensure_ascii=False, indent=2)


def save_to_mongodb(): # сохранить данные в БД MongoDB
    client = MongoClient()
    my_db = client['vk_api'] # создать/обратится к бд
    couple = my_db['couple'] # создать/обратится к коллекции
    # my_db.couple.drop()
    for people in func:
        couple.insert_one(people)
    print(list(couple.find())) # проверка


if __name__ == '__main__':
    save_to_file('couple.json')
    # save_to_mongodb()
