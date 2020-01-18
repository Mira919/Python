# Cоздать приложение Телефонная книга. В телефонную книгу (PhoneBook) надо добавлять контакты(Contact)

# 1. Класс Contact имеет следующие поля:
# Имя, фамилия, телефонный номер - обязательные поля;
# Избранный контакт - необязательное поле. По умолчанию False;
# Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, **kwargs.

# 2. Класс PhoneBook:
# Название телефонной книги - обязательное поле;
# Телефонная книга должна работать с классами Contact.

class Contact():

    def __init__(self, name, surname, phone_num, favourite=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        self.args = args
        self.kwargs = kwargs
        self.favourite = favourite
        if self.favourite is False:
            self.favourite_status = 'нет'
        else:
            self.favourite_status = 'да'

    def __str__(self):

        self.contact_str = 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Телефон: ' + self.phone_num + '\n' + 'В избранных: ' + self.favourite_status + '\n'

        if self.args:
            for i in self.args:
                self.contact_str += 'Дополнительный номер: ' + i

        if self.kwargs:
            self.contact_str += 'Дополнительная информация:\n'
            for key,value in self.kwargs.items():
                self.contact_str += '\t' + key + ': ' + value + '\n'

        return self.contact_str

class PhoneBook():

    def __init__(self, name):
        self.name = name
        self.contact_list = list()

    # показать все контакты телефонной книги
    def show_all_contacts(self):
        for contact in self.contact_list:
            print(contact)

    # добавить контакт в телефонную книги
    def add_contact(self, name, surname, phone_num,*args, **kwargs):
        self.contact_list.append(Contact(name, surname, phone_num,*args, **kwargs))
        print(f'Контакт {name} был добавлен')

    # удалить контакт по номеру из телефонной книги
    def delete_contact(self, phone_num):
        for contact in self.contact_list:
            if phone_num in contact.phone_num:
                self.contact_list.remove(contact)
                print(f'Контакт {contact.name} с номером {contact.phone_num} был удален\n')

    # вывести избранные контакты из телефонной книги
    def get_favourite(self):
        print('Избранные номера:')
        for contact in self.contact_list:
            if contact.favourite is True:
                print(f'\t{contact.phone_num}')

    # поиск контакта по имени и фамилии из телефонной книги
    def get_contact(self, name, surname):
        for contact in self.contact_list:
            if contact.name == name and contact.surname == surname:
                print(f'По вашему запросу был найден контакт:\n{contact}')

Mila_PhoneBook = PhoneBook('Мила') # создать телефонную книга Мила
Mira_PhoneBook = PhoneBook('Мира') # создать телефонную книга Мира

# добавить контакт в телефонную книгу Мила (закоменченные строчки после функции можно использовать вместо этой функции)
def add_contact(phone_book):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone_num = input('Введите телефонный номер: ')
    favourite = input('Добавить номер в избранные контакты?(да/нет): ')
    phone_book.add_contact(name, surname, phone_num)
add_contact(Mila_PhoneBook)
# Mila_PhoneBook.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
# Mila_PhoneBook.add_contact('Denis', 'Kaurow', '+75764523534', instagram='@denuska', email='denuska@gmail.com')
# Mila_PhoneBook.add_contact('Maria', 'Ankushina', '+79198648764', slack='@ankuuusha', email='denuska@gmail.com')

# показать все контакты телефонной книги Мила (закоменченные строчки после функции можно использовать вместо этой функции)
def show_all_contacts(phone_book):
    phone_book.show_all_contacts()
show_all_contacts(Mila_PhoneBook)
# Mila_PhoneBook.show_all_contacts()

# удалить контакт по номеру из телефонной книги Мила (закоменченные строчки после функции можно использовать вместо этой функции)
def delete_contact(phone_book):
    phone_num = str(input('Введите номер телефона контакта, которого хотите удалить (начиная с +7): '))
    phone_book.delete_contact(phone_num)
delete_contact(Mila_PhoneBook)
# Mila_PhoneBook.delete_contact('+71234567809')

# вывести избранные контакты из телефонной книги Мила (закоменченные строчки после функции можно использовать вместо этой функции)
def get_favourite(phone_book):
    phone_book.get_favourite()
get_favourite(Mila_PhoneBook)
# Mila_PhoneBook.get_favourite()

# поиск контакта по имени и фамилии из телефонной книги Мила (закоменченные строчки после функции можно использовать вместо этой функции)
def get_contact(phone_book):
    name = input('Введите имя контакта, которого хотите посмотреть: ')
    surname = input('Введите фамилию контакта, которого хотите посмотреть: ')
    phone_book.get_contact(name, surname)
get_contact(Mila_PhoneBook)
# Mila_PhoneBook.get_contact('Denis', 'Kaurow')

