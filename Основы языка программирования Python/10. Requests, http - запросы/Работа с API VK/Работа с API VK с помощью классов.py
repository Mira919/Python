from pprint import pprint
import requests

TOKEN = '5296a9c607f9f21de90e656a379680872dc4c0104880f655194bad219987787ccb133feca56d357888a36'

class User:
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN

    def get_params(self):
        return { # обязательный метод
            "access_token": self.TOKEN,
            'v': 5.89
        }

    def get_info(self):
        params = self.get_params()
        resp = requests.get(  # краткая информация о страничке
            'https://api.vk.com/method/users.get',
            params
        )
        return resp.json()

    def get_status(self):
        params = self.get_params()
        resp = requests.get(  # узнать статус пользователя
            'https://api.vk.com/method/status.set',
            params
        )
        return resp.json()
    
    def set_status(self, text):
        params = self.get_params()
        params['text'] = text
        resp = requests.get(  # изменить статус пользователя
            'https://api.vk.com/method/status.set',
            params
        )
        return resp.json()
    
Mira = User(TOKEN)

info = Mira.get_info()

pprint(info)
