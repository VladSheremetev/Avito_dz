from abc import ABC
import click
import numpy as np
from functools import wraps


def log(text: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time = np.random.randint(1, 30)
            print(text.format(time))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Функция ответственная за заказ"""
    print(f'🧑‍🍳 Приготовили за {np.random.randint(1, 20)}с!')
    if delivery:
        delivery_pizza(pizza)
    else:
        pickup(pizza)


@log('🛵 Доставили за {}с!')
def delivery_pizza(pizza: str):
    """Функция ответственная за доставку пиццы"""
    return None


@log('🏠 Забрали за {}с!')
def pickup(pizza: str):
    """Функция ответственная за самовывоз пиццы"""
    return None


@cli.command()
def menu():
    """Выводит меню"""

    list_pizza = [Margherita(), Pepperoni(), Hawaiian()]

    for pizza in list_pizza:
        type_pizza = pizza.__class__.__name__
        symbol_pizza = pizza.symbol
        composition_pizza = pizza.dict().keys()
        print(f"- {type_pizza} {symbol_pizza}: {', '.join(composition_pizza)}")


class Pizza(ABC):
    """Абстрактный класс пиццы"""
    _composition = {}
    _possible_size = ['XL', 'L']

    def __init__(self, size: str = 'L'):
        if size in self._possible_size:
            self._size = size
        else:
            raise TypeError("Нет такого размера пиццы")

    def dict(self):
        """Возвращает список ингредиентов пиццы"""
        return self._composition

    def __eq__(self, other):
        uniqueness_composition = set(self._composition.keys()) - set(other._composition.keys())
        if uniqueness_composition or self._size != other._size:
            return False
        else:
            return True


class Margherita(Pizza):
    """Класс ответственный за пиццу Маргариту"""
    _composition = {'tomato sauce': '', 'mozzarella': '', 'tomatoes': ''}
    _symbol = '🧀'

    def __init__(self, size: str = 'L'):
        super().__init__(size)

    @property
    def symbol(self):
        return self._symbol


class Pepperoni(Pizza):
    """Класс ответственный за пиццу Пеперонни"""
    _composition = {'tomato sauce': '', 'mozzarella': '', 'pepperoni': ''}
    _symbol = '🍕'

    def __init__(self, size: str = 'L'):
        super().__init__(size)

    @property
    def symbol(self):
        return self._symbol


class Hawaiian(Pizza):
    """Класс ответственный за пиццу Гавайскую"""
    _composition = {'tomato sauce': '', 'mozzarella': '', 'chicken': '', 'pineapples': ''}
    _symbol = '🍍'

    def __init__(self, size: str = 'L'):
        super().__init__(size)

    @property
    def symbol(self):
        return self._symbol


if __name__ == "__main__":
    cli()
