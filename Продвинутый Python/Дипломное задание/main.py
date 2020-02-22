import vk
import time
import datetime
import json
from pymongo import MongoClient

access_token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
v = '5.103'

session = vk.Session(access_token)
api = vk.API(session, v=v)


# получаем страницу пользователя, которому надо найти пару
def get_user(id): 
    start_time = datetime.datetime.now()
    user = api.users.get(user_ids=id, fields='bdate,sex,city,interests')
    groups = api.users.getSubscriptions(user_id=id, extended=1)
    time.sleep(1.5)
    for i in user:
        i['groups'] = groups
    print(f'Функция get_user исполнялась {datetime.datetime.now() - start_time}')
    return user[0]


# ищем пару по критериям
def get_couple(): 
    start_time = datetime.datetime.now()
    user = get_user('169989152')
    couple = []

    if user['sex'] == 1: # определить пол
        sex = 2
    else:
        sex = 1

    users = api.users.search(count=150, sex=sex, city=user['city']['id'], fields='bdate,sex,city,domain') # count(кол-во), sex(пол), сity(город), bdate(день рождение), domain(короткие адрес)
    for people in users['items']:
        if not people['is_closed']: # проверка что страница не закрыта
            try:
                age_user = str((datetime.datetime.today() - datetime.datetime.strptime(user['bdate'], '%d.%m.%Y')) / 365)[:2]
                age_people = str((datetime.datetime.today() - datetime.datetime.strptime(people['bdate'], '%d.%m.%Y'))/365)[:2]
                if 6 > int(age_user) - int(age_people) > -6:  # проверка по возрасту (+- 6 лет)
                    couple.append(people)
            except:
                pass
    print(f'Функция get_couple исполнялась {datetime.datetime.now() - start_time}')
    return couple[:10]


# Получаем ссылку на пользователя и топ 3 фотографии
def get_url_photo():
    users = get_couple()
    start_time = datetime.datetime.now()
    list_to_save = [] # конечный результат

    for user in users:
        top3_like = [] # лайки фоток по убыванию
        user_photo = api.photos.get(owner_id=user['id'], album_id='profile', extended = 1) # получаем фотки со страницы пользователя
        time.sleep(1.5)
        for photo in user_photo['items']:
            top3_like.append(photo['likes']['count']) # добавляем лайки фоток
        top3_like.sort(reverse=True) # сортировка лайков по убыванию

        top_dict = {} # id: ссылка на пользователя, photos: [ссылки на топ 3 фотографии]
        url_list = [] # список для хранения ссылок на фотки
        for photo in user_photo['items']:
            if photo['likes']['count'] in top3_like[:3]: # если фото в топ 3 лайков, то добавляем ссылку на фото
                url_list.append(photo['sizes'][0]['url'])
        top_dict['id'] = 'https://vk.com/' + user['domain'] # добавляем ссылку на пользователя
        top_dict['photos'] = url_list[:3] # добавляем 3 ссылки на фотографии
        list_to_save.append(top_dict)
    print(f'Функция get_photo исполнялась {datetime.datetime.now() - start_time}')
    return list_to_save


func = get_url_photo()


# сохранить данные в файл JSON
def save_to_file(file_name): 
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(func, file, ensure_ascii=False, indent=2)


# сохранить данные в БД MongoDB
def save_to_mongodb(): 
    client = MongoClient()
    my_db = client['vk_api'] # создать/обратится к бд
    couple = my_db['couple'] # создать/обратится к коллекции
    # my_db.couple.drop()
    for people in func:
        couple.insert_one(people)
    print(list(couple.find())) # проверка


if __name__ == '__main__':
    save_to_file('couple.json')
    save_to_mongodb()
