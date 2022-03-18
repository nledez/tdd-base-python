import unittest
from src.main import main

class MainTestCases(unittest.TestCase):

    def test_function_return(self):
        '''function should return Hello World'''
        self.assertEqual(main(1), "Hello World")

    def test_function_exception(self):
        '''function should return an exception on value 2'''
        try:
            main(2)
        except Exception:
            pass
        else:
            raise "main should return an expection when called with value 2"
