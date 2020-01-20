# Следует протестировать основные функции программы переводчика из main.py
import unittest
import main

class TestSecretaryProgram(unittest.TestCase):

    # проверка перевода с русского на английский
    def test_translate_ru_to_eng(self):
        translate = main.translate_to_file("Я пошла гулять", "ru-en")
        self.assertEqual(translate, 'I went for a walk')
        print('Результат перевода с русского на английский правильный')

    # проверка перевода с русского на испанский
    def test_translate_ru_to_es(self):
        translate = main.translate_to_file("Я пошла гулять", "ru-es")
        self.assertEqual(translate, 'Me fui a pasear')
        print('Результат перевода с русского на испанский правильный')

    # проверка перевода с французского на русский
    def test_translate_fr_to_ru(self):
        translate = main.translate_to_file("Je suis allé me promener", "fr-ru")
        self.assertEqual(translate, 'Я пошел гулять')
        print('Результат перевода с французского на русский правильный')

    # проверка статус кода функции
    def test_translate_status_code(self):
        translate_status_code = main.translate_to_file_status_code("Je suis allé me promener", "fr-ru")
        self.assertEqual(translate_status_code, 200)
        print('Код ответа соответствует 200')

if __name__ == '__main__':
    unittest.main()
