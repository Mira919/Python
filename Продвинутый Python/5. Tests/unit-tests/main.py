documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },
    {
        "type": "invoice",
        "number": "11-2",
        "name": "Геннадий Покемонов"
    },
    {
        "type": "insurance",
        "number": "10006",
        "name": "Аристарх Павлов"
    }
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

# команда P, которая спросит номер документа и выведет имя человека, которому он принадлежит
def number_document(document):
    document_input = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == document_input:
            return document['name']
    return "Документа нет"

# команда L, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def all_document(document):
    for doc in document:
        print(doc["type"] + ' ' + doc["number"] + ' ' + doc["name"])

# команда S, команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelves(document):
    document_input = input('Введите номер документа: ')
    for directory in document.items():
        for number_doc in directory[1]:
            if number_doc == document_input:
                return "Документ находится на полке №" + directory[0]
    return "Данный документа не найден"

# команда A, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add(document, directory):
    number_input = input('Введите номер документа: ')
    type_input = input('Введите тип документа: ')
    name_input = input('Введите имя владельца: ')
    shelves_input = input('Введите номер полки, на котором будет храниться документ: ')

    new_dict = {}
    new_dict['type'] = type_input
    new_dict['number'] = number_input
    new_dict['name'] = name_input

    shelves = []
    for direct in directory.keys():
        shelves.append(direct)
    if shelves_input not in shelves:
        print("Такой полки нет, документ не был добавлен!")
    else:
        document.append(new_dict)
        directory[shelves_input].append(number_input)
    print(document)
    print(directory)

# команда n, которая выводит имена всех владельцев документов и проверяет есть ли поле "name" у документа.
def name_people(document):
    for doc in document:
        try:
            print(doc["name"])
        except KeyError:
            print(f"У документа номер {doc['number']} отсутствует поле 'name'!")
# чтобы пользователь смог ввести команду
# while True:
#     user_input = input('Введите команду: ')
#     if user_input == 'p':
#         print(number_document(documents))
#     elif user_input == 'l':
#         all_document(documents)
#     elif user_input == 's':
#         print(shelves(directories))
#     elif user_input == 'a':
#         add(documents, directories)
#     elif user_input == 'n':
#         name_people(documents)
#     elif user_input == 'q':
#         print('Пока!')
#         break