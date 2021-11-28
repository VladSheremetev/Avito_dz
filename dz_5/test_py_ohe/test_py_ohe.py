import pytest
from ohe import fit_transform


def test_fit_transform_0():
    data = []
    exp_transformed = []
    assert fit_transform(data) == exp_transformed


def test_fit_transform_1():
    data = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(data) == exp_transformed


def test_fit_transform_2():
    data = [1]
    exp_transformed = [
        (1, [1]),
    ]
    assert fit_transform(data) == exp_transformed


def test_fit_transform_3():
    data = [1, '', ['c']]
    with pytest.raises(TypeError):
        fit_transform(data)


def test_fit_transform_error():
    with pytest.raises(TypeError):
        fit_transform()


if __name__ == '__main__':
    pass
