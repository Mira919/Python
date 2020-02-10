import vk
import time

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
        users_id.append(i+1)

    users_list = []
    for user_id in users_id:
        user = api.users.get(user_ids = user_id, fields = 'bdate,sex,city,interests')
        if user[0]['first_name'] != 'DELETED': # не берем пользователя если он удален
            if user[0]['is_closed'] == False: # не берем если у пользователя закрыта страница
                groups = api.users.getSubscriptions(user_id=user_id, extended=1)
                for i in user:
                    i['groups'] = groups
                users_list.append(user)
                time.sleep(3)
    return users_list


# print(get_user('169989152'))
# print(get_users())
