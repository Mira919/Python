# Получаем разные данные с аккаунтов пользователей. В запросах, в ссылках надо менять предпоследнее слово (users, griends и тд.)

from urllib.parse import urlencode
from pprint import pprint
import requests

URL = "https://oauth.vk.com/authorize" # https://vk.com/dev/implicit_flow_user
PARAMS = {
    'client_id': 7230196, # Мои приложения -> Создать приложение и выбрать standalone -> Настройки
    'display': 'page',
    'response_type': 'token',
    'scope': 'status' # какие разрешение прав доступа запросить
}
print('?'.join((URL, urlencode(PARAMS)))) # создаем ссылку соединяя ссылку и параметры

TOKEN = '5296a9c607f9f21de90e656a379680872dc4c0104880f655194bad219987787ccb133feca56d357888a36' # перейти по ссылке выше и нажать разрешить, далее взять токен из адресной строки

params = { # обязательные данные
    'access_token': TOKEN,
    'v': 5.89,
}

resp = requests.get( # краткая информация о страничке
    'https://api.vk.com/method/users.get',
    params = params
)
pprint(resp.json())

params['text'] = 'Cool'
resp = requests.get( # изменить статус пользователя на Cool
    'https://api.vk.com/method/status.set',
    params = params
)
pprint(resp.json())

resp = requests.get( # узнать статус пользователя
    'https://api.vk.com/method/status.get',
    params = params
)
pprint(resp.json())
