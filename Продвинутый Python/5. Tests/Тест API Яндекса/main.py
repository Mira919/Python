# Переводчик онлайн

import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"  # API яндекс переводчика

# функция для перевода
def translate_to_file(text, lang):  # lang - с какого на какой язык, text - текст для перевода

    resp_translate = requests.post(URL, params={  # запрос на перевод
        "key": "trnsl.1.1.20191128T170444Z.c56d359e1889b3b7.8fccca1aa4fe51ff1bb52de2213efc89f26608ff", # стандартный ключ, берется на сайте
        "text": text,  # текст на перевод
        "lang": lang})  # с какого языка на какой

    resp_translate = resp_translate.json()["text"]
    resp_translate = ' '.join(resp_translate)  # перевести список в строку
    return resp_translate

# функция для вывода статус кода
def translate_to_file_status_code(text, lang):  # lang - с какого на какой язык, text - просто любой текст

    resp_translate = requests.post(URL, params={  # запрос на перевод
        "key": "trnsl.1.1.20191128T170444Z.c56d359e1889b3b7.8fccca1aa4fe51ff1bb52de2213efc89f26608ff", # стандартный ключ, берется на сайте
        "text": text,  # текст на перевод
        "lang": lang})  # с какого языка на какой

    return resp_translate.status_code
