import json

class Url_wiki:
    def __init__(self, data):
        self.data = data.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        dict = {}
        item = self.data.__next__()
        item = item['name']['common']
        dict[item] = 'https://ru.wikipedia.org/wiki/' + item
        return dict

with open('countries.json', encoding = 'utf-8-sig') as f:
    data = json.load(f)

list_country = []
with open('country-wiki.json', 'w', encoding='utf-8-sig') as f:
    for country in Url_wiki(data):
        list_country.append(country)
    json.dump(list_country, f, ensure_ascii=False, indent=8)

