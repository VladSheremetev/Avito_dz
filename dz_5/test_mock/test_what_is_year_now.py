from wyn import What_is_year_now
from unittest.mock import patch
import unittest


class TestWY(unittest.TestCase):

    @patch.object(What_is_year_now, "datetime_str", new='01.03.2021')
    def test_what_is_year_now_0(self):
        print(What_is_year_now().what_is_year_now())
        self.assertEqual(What_is_year_now().what_is_year_now(), 2021)


if __name__ == '__main__':
    unittest.main()
