# Следует протестировать основные функции программы main.py

import unittest
import main
import sys # для того, чтобы проверять функции которые делают print, а не return
from contextlib import contextmanager # для того, чтобы проверять функции которые делают print, а не return
from io import StringIO # для того, чтобы проверять функции которые делают print, а не return

@contextmanager # для того, чтобы проверять функции которые делают print, а не return
def captured_output(): # для того, чтобы проверять функции которые делают print, а не return
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestSecretaryProgram(unittest.TestCase):

    # проверка на вывод
    def test_one_document(self):
        with captured_output() as (out, err): # для того, чтобы проверять функции которые делают print, а не return
            main.all_document([{ # вызвать функцию и дать данные
                "type": "insurance",
                "number": "10006",
                "name": "Аристарх Павлов"
            }])
            output = out.getvalue().strip()
            self.assertEqual(output, 'insurance 10006 Аристарх Павлов')

    # проверка на перенос строки
    def test_all_document(self):
        with captured_output() as (out, err): # для того, чтобы проверять функции которые делают print, а не return
            main.all_document(main.documents) # вызвать функцию и дать данные из документа main.py
            output = out.getvalue().strip()
            self.assertIn('\n', output)

    # проверка на вывод исключения KeyError если нет строки NAME
    def test_get_exception_name_people(self):
        with self.assertRaises(KeyError):
            main.all_document([{ # вызвать функцию и дать данные
                "type": "invoice",
                "number": "11-2",
            }])

    # проверка на вывод имен
    def test_name_people(self):
        with captured_output() as (out, err):
            main.name_people(main.documents) # вызвать функцию и дать данные
            output = out.getvalue().strip()
            self.assertEqual(output, 'Василий Гупкин\nГеннадий Покемонов\nАристарх Павлов')


if __name__ == '__main__':
    unittest.main()
