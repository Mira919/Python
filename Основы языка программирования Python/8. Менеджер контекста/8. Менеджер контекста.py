# 1. Вычисляет время начала, время завершения и продолжительность работы кода

import datetime
class MyOpen:
    def __init__(self, path, encoding='utf-8'):
        self.path = path
        self.encoding = encoding

    def __enter__(self): # вызовется когда зайдем в контекст, передает обьект в переменную marks_file
        self.file = open(self.path, encoding=self.encoding)
        self.start = datetime.datetime.now()
        print(f'Code launch time: {self.start}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb): # вызовется когда выйдем из контекста
        self.file.close()
        self.finish = datetime.datetime.now()
        print(f'Document completed in: {self.finish}')
        print(f'Time spent executing code: {self.finish - self.start} ')

if __name__ == '__main__':
    with MyOpen('test.csv') as marks_file:
        marks = marks_file.read() # просто прочитать файл

# 2. Написать программу, использующая менеджер контекста(Вычисляет и выводит время начала, время завершения и продолжительность работы кода). Использована задача по составлению пар из двух списков (с помощью ZIP)

import datetime
class MyContextManager:
    def __init__(self, boys, girls):
        self.boys = boys
        self.girls = girls

    def __enter__(self):
        self.start = datetime.datetime.now()
        print(f'Код начал работу в: {self.start}')
        self.boys = sorted(self.boys)
        self.girls = sorted(self.girls)

        self.boys_girls = zip(self.boys, self.girls)
        self.boys_girls = list(self.boys_girls)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if len(self.boys) != len(self.girls):
            print('Кто - то может остаться без пары!')
        else:
            for couple in self.boys_girls:
                print(couple[0], ' и ', couple[1])

        self.finish = datetime.datetime.now()
        print(f'Код закончил работу в: {self.finish}')
        print(f'Продолжительность выполнения кода: {self.finish - self.start} ')
if __name__ == '__main__':
    with MyContextManager(['Peter', 'Alex', 'John', 'Arthur', 'Richard'],['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']) as couple:
        print('Пары составлены')

# Сообщения преподователя: Зашивать основную логику в enter и exit возможно не лучшая идея. Обратите внимание, что enter в этом примере ни чего не возвращает, поэтому в as couple запишется None

# 3. Записывает появившиеся в ходе выполнения программы ошибки в отдельный файл, а также время когда была произведена ошибка

import datetime
class Loger:
  def __init__(self, path):
    self.path = path

  def __enter__(self): # вызовется когда зайдем в контекст, передает обьект в переменную log
    self.file = open(self.path, 'a', encoding='utf-8')
    return self

  def __exit__(self, exc_type, exc_val, exc_tb): # вызовется когда выйдем их контекста
    if exc_type:
      self.file.write(f'{datetime.datetime.now() }ERROR {exc_type} {exc_val}/n')
    self.file.close()

  def write(self,row):
    self.file.write(f'.{datetime.datetime.now() } {row}')

if __name__ == '__main__':
  with Loger('log.txt') as log:
    a = 2 + 1
    log.write(f'do math {a}')
    a / 0
    log.write(f'do math {a}')
