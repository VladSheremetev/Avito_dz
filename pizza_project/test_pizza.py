import pizza_project as pz
import pytest
from mock import patch


def test_margherita():
    assert pz.Margherita().dict() == {'tomato sauce': '', 'mozzarella': '', 'tomatoes': ''}


def test_pepperoni():
    assert pz.Pepperoni().dict() == {'tomato sauce': '', 'mozzarella': '', 'pepperoni': ''}


def test_hawaiian():
    assert pz.Hawaiian().dict() == {'tomato sauce': '', 'mozzarella': '', 'chicken': '', 'pineapples': ''}


def test_eq():
    a = pz.Hawaiian('XL')
    b = pz.Pepperoni('L')
    c = pz.Hawaiian('XL')

    assert not (a == b)
    assert (a == c)


def test_pickup():
    patch('pz.log', lambda x: x)
    assert not pz.pickup('peperoni')


def test_delivery_pizza():
    patch('pz.log', lambda x: x)
    assert not pz.delivery_pizza('peperoni')


def test_order():
    patch('cli.command', lambda x: x)
    patch('click.option', lambda x: x)
    patch('click.argument', lambda x: x)
    patch('pz.log', lambda x: x)
    assert pz.order('peperoni', True) == ':bike: Доставили за 2с!'
