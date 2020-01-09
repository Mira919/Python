import json

# with open('countries.json', encoding = 'utf-8-sig') as f:
#     data = json.load(f)
# for country in data:
#     print(country['name']['common'])

class Url_wiki:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return self

    def __next__(self):

        counries_list = []


        with open(self.file, encoding='utf-8-sig') as f:
            data = json.load(f)
        iter = data.__iter__()
        item = iter.__next__()
        counries_list.append(item)
        return(item['name']['common'])

for i in Url_wiki('countries.json'):
    print(i)
