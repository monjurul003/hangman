import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        word = main.get_valid_words()

        self.assertTrue( '-' not in word and ' ' not in word)


if __name__ == '__main__':
    unittest.main()
