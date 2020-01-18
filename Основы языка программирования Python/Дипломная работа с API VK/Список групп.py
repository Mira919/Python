# Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей. 
# В качестве жертвы, на ком тестировать, можно использовать: https://vk.com/eshmargunov, токен: 73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1

# Итог: Файл groups.json в формате:
# [
#     {
#     “name”: “Название группы”, 
#     “gid”: “идентификатор группы”, 
#     “members_count”: количество_участников_сообщества
#     },
#     {
#     …
#     }
# ]

import time
import json
from pprint import pprint
import requests

TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

def get_params(TOKEN): # обязательные параметры
    return {
    'access_token': TOKEN,
    'v': 5.89,
    }

def get_groupINFO_user(): # получаем информацию о группах пользователя
    params = get_params(TOKEN)
    params['extended'] = 1
    params['fields'] = 'members_count'
    groups_user = requests.get(
        'https://api.vk.com/method/groups.get',
        params = params
    )
    groups_user = groups_user.json()['response']
    groups_user = groups_user['items']
    return groups_user

def get_friendID(): # получаем id друзей пользователя
    params = get_params(TOKEN)
    friends_user = requests.get(
        'https://api.vk.com/method/friends.get',
        params = params
    )
    friends_user = friends_user.json()['response']
    friends_user = friends_user['items']
    return friends_user

def get_groupID_friends(): # получаем id групп друзей пользователя
    params = get_params(TOKEN)
    list_group_friend = []
    for friend in get_friendID():
        params['user_id'] = friend
        try: # чтобы поймать ошибку когда страница пользователя закрыта
            friend_group = requests.get(
                'https://api.vk.com/method/groups.get',
                params = params
            )
            friend_group = friend_group.json()['response']
            friend_group = friend_group['items']
            list_group_friend += friend_group
            print('Идет поиск групп у пользователя c id:', params['user_id']) # показывает что программа не зависла
            time.sleep(2) # чтобы не было ошибки: слишком много обращений к API (Too many requests per second)
        except KeyError:
            print(f"У пользователя c id {params['user_id']} закрыта страница")
    return list_group_friend

def get_group(): # получаем группы, где состоит пользователь, но не состоит никто из его друзей
    list = []
    groups_user = get_groupINFO_user()
    list_group_friend = get_groupID_friends()
    for group in groups_user:
        if group['id'] not in list_group_friend:
            dict = {}
            dict['name'] = group['name']
            dict['gid'] = group['id']
            dict['members_count'] = group['members_count']
            list.append(dict)
    return list

with open('groups.json', 'w', encoding='utf-8') as file:
    json.dump(get_group(), file, ensure_ascii=False, indent=2)

with open('groups.json', encoding = 'utf-8-sig' ) as file:
     data = json.load(file)
pprint(data)
