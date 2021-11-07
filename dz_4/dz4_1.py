import random


class Pokemon:
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


class Digimon:
    def __init__(self, name: str, digitype='No name'):
        self.name = name
        self.digitype = digitype
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def __str__(self):
        return f'{self.name}/{self.digitype}'

    def inc_exp(self, value: int):
        self._exp += value * 8


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)
    print(bulbasaur.exp)
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
