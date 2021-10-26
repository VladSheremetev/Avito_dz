from pprint import pprint
from typing import List, Iterable, Tuple, Dict


class CountVectorizer:
    def __init__(self):
        self._unique_words = []
        self._count_word_in_text = []

    def fit_transform(self, list_text: List[str]):
        self._unique_words, self._count_word_in_text = self.count_words_in_list_text(list_text)
        return self._count_word_in_text

    def get_feature_names_out(self):
        return self._unique_words

    @staticmethod
    def count_words_in_list_text(list_text: Iterable) -> Tuple[List[str], List[str]]:
        """Функция, которая считает количество отдельных слов в последовательности текстов"""
        unique_words = get_unique_words_in_list_text(list_text)
        count_word_in_text = []
        for text in list_text:
            zero_values(unique_words)
            for word in text.split():
                word = word.strip('.,;:-?"!').lower()
                unique_words[word] += 1
            count_word_in_text.append(list(unique_words.values()))

        return list(unique_words.keys()), count_word_in_text


def zero_values(dict_words: Dict[str, int]) -> None:
    """Функция, которая обнуляет счётчик слов"""
    for key in dict_words.keys():
        dict_words[key] = 0


def get_unique_words_in_list_text(list_text: List[str]) -> Dict[str, int]:
    """Функция, которая создаёт словарь со всеми уникальными словами во всех последовательностях текстов\
    в качестве ключей, а счётчик слов в качестве values
    """
    unique_words = {}
    for text in list_text:
        for word in text.split():
            word = word.strip('.,;:-?"!').lower()
            unique_words[word] = 0
    return unique_words


if __name__ == '__main__':
    corpus = [
        'This is the first document.',
        'This document is the second document.',
        'And this is the third one.',
        'Is this the first document?',
    ]
    s = CountVectorizer()
    pprint(s.fit_transform(corpus))
    pprint(s.get_feature_names_out())
