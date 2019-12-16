# Программа которая берет песни любого исполнителя из itunes и сохранять картинки каждой песни в новую папке (папку Covers надо создать)

import os
import requests

URL = "http://itunes.apple.com/search"
term = "Монеточка"

resp = requests.get(URL, params = {"term": term}) # передаем параметры

if resp.status_code >= 400:
    raise RuntimeError("Возникла ошибка сервера")

# проитерироваться по каждой песне и получить название песни, альбома и артиста(ов) каждой песни
resp_json = resp.json()
for i, song in enumerate(resp_json["results"], 1): # 1 - чтобы с первой цифры начиналась нумерация
    print(f"Обрабатывается песня №{i}")
    track_name = song["trackName"]
    album_name = song.get("collectionName")
    artist_name = song['artistName']

    name_for_cover = f"{artist_name}, {track_name}, {album_name}.jpg"

    cover_url = song["artworkUrl100"] # получаем поле со ссылкой на картинку песни

    cover_filename = os.path.join("Covers", name_for_cover) # соединяет пути, дает название файлу с картинкой: первый параметр - название папки, второй - как будет называться файл
    with open(cover_filename, "wb") as f: # режим байтовый
        img_resp = requests.get(cover_url) # получить картинку
        f.write(img_resp.content) # записать картинку в файл
