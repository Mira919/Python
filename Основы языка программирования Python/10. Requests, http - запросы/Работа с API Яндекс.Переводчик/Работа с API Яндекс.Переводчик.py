# Есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком. Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.
    
import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate" # API яндекс переводчика

def translate_to_file(file, lang, text): # file - название файла который надо перевести, lang - с какого на какой язык, text - просто любой текст
    with open(file, 'r') as f: 
        translate = f.read() # читаем файл и записываем содержимое в переменную

    resp_translate = requests.post(URL, params = { # запрос на перевод
                                    "key": "trnsl.1.1.20191128T170444Z.c56d359e1889b3b7.8fccca1aa4fe51ff1bb52de2213efc89f26608ff", # стандартный ключ, берется на сайте
                                    "text": translate, # содержимое файла
                                    "lang": lang}) # с какого языка на какой
    with open("RU.txt", "a") as f: # файл куда сохранить перевод
        resp_translate = resp_translate.json()["text"]
        resp_translate = ' '.join(resp_translate) # перевести список в строку
        f.write(f"{text}: {resp_translate}\n")

translate_to_file("DE.txt", "de-ru", "Перевод с Немецкого")
translate_to_file("ES.txt", "es-ru", "Перевод с Испанского")
translate_to_file("FR.txt", "fr-ru", "Перевод с Французского")
