from abc import abstractmethod
import random


class AnimeMon:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    @abstractmethod
    def inc_exp(cls):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    def __str__(self):
        return f'{self.name}/{self.poketype}'

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value: int):
        self._exp += value * 2


class Digimon(AnimeMon):
    def __init__(self, name: str, digitype='No name'):
        self.name = name
        self.digitype = digitype
        self._exp = 0

    def __str__(self):
        return f'{self.name}/{self.digitype}'

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value: int):
        self._exp += value * 8


def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)
    print(bulbasaur.exp)
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
