import unittest
import main

class TestSecretaryProgram(unittest.TestCase):

    def test_get_number_document(self):
        document = main.all_document(main.documents)
        self.assertEqual(document, ' ')

if __name__ == '__main__':
    unittest.main()

# def abc():
#     document = main.all_document(main.documents)
# abc()