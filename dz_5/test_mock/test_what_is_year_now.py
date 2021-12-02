from wyn import WhatIsYearNow
from unittest.mock import patch
import io
import urllib.request
import unittest


class TestWY(unittest.TestCase):

    @patch('wyn.WhatIsYearNow.get_data', return_value={"currentDateTime": "01.03.2021"})
    def test_what_is_year_now_0(self, func):
        self.assertEqual(WhatIsYearNow().what_is_year_now(), 2021)

    @patch('wyn.WhatIsYearNow.get_data', return_value={"currentDateTime": "01.03/2021"})
    def test_what_is_year_now_1(self, func):
        with self.assertRaises(ValueError):
            self.assertRaises(WhatIsYearNow().what_is_year_now())

    @patch('wyn.WhatIsYearNow.get_data', return_value={"currentDateTime": "2021-03-01"})
    def test_what_is_year_now_2(self, func):
        self.assertEqual(WhatIsYearNow().what_is_year_now(), 2021)

    @patch('wyn.WhatIsYearNow.get_data', return_value={"currentDateTime": "2021-03-01"})
    def test_what_is_year_now_3(self, func):
        self.assertIsInstance(WhatIsYearNow().what_is_year_now(), int)

    def test_what_is_year_now_4(self):
        date = io.StringIO('{"currentDateTime": "2021-03-01"}')
        with patch.object(urllib.request, 'urlopen', return_value=date):
            self.assertEqual(WhatIsYearNow().get_data(), {"currentDateTime": "2021-03-01"})


if __name__ == '__main__':
    unittest.main()
