import unittest
import gazette_processor

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.gp = Gazette('test_file.txt', '', '')


    def test_get_list_of_pages(self):
        result = self.gp.get_list_of_pages()
        len_result = len(result)
        self.assertEqual(3, len_result, "A quantidade de paginas não retornou o valor correto")



if __name__ == '__main__':
    unittest.main()
