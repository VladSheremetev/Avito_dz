import pizza_project as pz
import pytest


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
