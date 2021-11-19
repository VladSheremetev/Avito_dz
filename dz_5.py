from operator import add
from functools import partial
from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __rmul__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, *args):
        self.rgb = tuple(map(self._normalize, args))

    def _normalize(self, value):
        return max(min(255, value), 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        raise TypeError('Типы разные')

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Color(*map(add, self.rgb, other.rgb))
        raise TypeError('Типы разные')

    def __hash__(self):
        return hash(self.rgb)

    def _contrast(self, value, c=1):
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        return int(F * (value - 128) + 128)

    def __mul__(self, value):
        if isinstance(value, float):
            contrast = partial(self._contrast, c=value)
            return Color(*map(contrast, self.rgb))

    def __rmul__(self, value):
        return self.__mul__(value)

    def __repr__(self):
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}'


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)
    print(red == Color(255, 0, 0))
    print(Color(0, 255, 0) + Color(255, 0, 0))
    print(0.5 * red)
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)

    color_list = [orange1, red, green, orange2]
    set(color_list)
