from wyn import What_is_year_now
from unittest.mock import patch
import unittest


class TestWY(unittest.TestCase):

    @patch('wyn.What_is_year_now.get_data', return_value='01.03.2021')
    def test_what_is_year_now_0(self, func):
        self.assertEqual(What_is_year_now().what_is_year_now(), 2021)

    @patch('wyn.What_is_year_now.get_data', return_value='01.03/2021')
    def test_what_is_year_now_1(self, func):
        with self.assertRaises(ValueError):
            self.assertRaises(What_is_year_now().what_is_year_now())

    @patch('wyn.What_is_year_now.get_data', return_value='2021-03-01')
    def test_what_is_year_now_2(self, func):
        self.assertEqual(What_is_year_now().what_is_year_now(), 2021)

    @patch('wyn.What_is_year_now.get_data', return_value='2021-03-01')
    def test_what_is_year_now_3(self, func):
        self.assertIsInstance(What_is_year_now().what_is_year_now(), int)

    def test_what_is_year_now_4(self):
        date = What_is_year_now().get_data()
        self.assertEqual(date[:10], '2021-11-29')


if __name__ == '__main__':
    unittest.main()
