import pytest
from morse import decode


@pytest.mark.parametrize('mess,ans', [
    ('... --- ...', 'SOS'),
    ('.- .- .-  -... . ... -  . -.. ..- -.-. .- - .. --- -. .- .-..  .--. .-. --- .--- . -.-. -',
     'AAA BEST EDUCATIONAL PROJECT'),
    ('.- .- .- ..--- ----- ..--- .----', 'AAA2021'),
])
def test_decode(mess: str, ans: str):
    assert decode(mess) == ans


if __name__ == '__main__':
    pass
