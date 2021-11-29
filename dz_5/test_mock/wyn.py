import urllib.request
import json


class What_is_year_now():
    API_URL = 'http://worldclockapi.com/api/json/utc/now'

    YMD_SEP = '-'
    YMD_SEP_INDEX = 4
    YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

    DMY_SEP = '.'
    DMY_SEP_INDEX = 5
    DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)

    @staticmethod
    def get_data() -> str:
        with urllib.request.urlopen(What_is_year_now.API_URL) as resp:
            resp_json = json.load(resp)

        return resp_json['currentDateTime']

    def what_is_year_now(self) -> int:
        """
        Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
        Предположим, что currentDateTime может быть в двух форматах:
          * YYYY-MM-DD - 2019-03-01
          * DD.MM.YYYY - 01.03.2019
        """

        datetime_str = self.get_data()
        if datetime_str[self.YMD_SEP_INDEX] == self.YMD_SEP:
            year_str = datetime_str[self.YMD_YEAR_SLICE]
        elif datetime_str[self.DMY_SEP_INDEX] == self.DMY_SEP:
            year_str = datetime_str[self.DMY_YEAR_SLICE]
        else:
            raise ValueError('Invalid format')

        return int(year_str)


if __name__ == '__main__':
    year = What_is_year_now().what_is_year_now()
    exp_year = 2021
    print(What_is_year_now.__dict__)
    print(year)
    assert year == exp_year
