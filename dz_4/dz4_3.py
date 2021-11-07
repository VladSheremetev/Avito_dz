import json


class Errorprice(BaseException):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class ColorizeMixin:
    repr_color_code = 32

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m {self.title} | {self.price} ₽'


class json_transform(object):
    def __init__(self, kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                value = json_transform(value)
            setattr(self, key, value)


class Advert(ColorizeMixin, json_transform):
    def __init__(self, kwargs={}):
        self.__dict__ = json_transform(kwargs).__dict__
        is_price = self.__dict__.get('price')
        if is_price and self.__dict__['price'] < 0:
            raise Errorprice('ValueError: price must be >= 0')
        else:
            setattr(self, 'price', is_price or 0)

        def __repr__(self):
            return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
    # lesson_ad.__dict__
    iphone_ad = Advert({"title": "iPhone X", "price": 100,})
    print(iphone_ad.price)
    print(lesson_ad)
