from pprint import pprint
from collections.abc import Iterable


# from collections.abc import Sequence


class CountVectorizer:
    def __init__(self, input='content', encoding='utf-8', lowercase=True):
        self._input = input
        self._encoding = encoding
        self._lowercase = lowercase
        self._unique_words = []
        self._count_word_in_text = []

    def fit_transform(self, args):
        list_text = get_data(args, self._input, self._encoding)
        self._unique_words, self._count_word_in_text = count_words_in_list_text(list_text, self._lowercase)
        return self._count_word_in_text

    def get_feature_names_out(self):
        return self._unique_words


def count_words_in_list_text(list_text: Iterable, lowercase: bool) -> (list, list):
    """Функция, которая считает количество отдельных слов в последовательности текстов"""

    unique_words = get_unique_words_in_list_text(list_text, lowercase)
    count_word_in_text = []
    for text in list_text:
        zero_values(unique_words)
        for word in text.split():
            word = word.strip('.,;:-?"!')
            if lowercase:
                word = word.lower()
            unique_words[word] += 1
        count_word_in_text.append(list(unique_words.values()))

    return list(unique_words.keys()), count_word_in_text


def zero_values(dict_words):
    """Функция, которая обнуляет счётчик слов"""
    for key in dict_words.keys():
        dict_words[key] = 0


def get_unique_words_in_list_text(list_text: list, lowercase: bool) -> dict:
    """Функция, которая создаёт словарь со всеми уникальными словами во всех последовательностях текстов\
    в качестве ключей, а счётчик слов в качестве values
    """
    unique_words = {}
    for text in list_text:
        for word in text.split():
            word = word.strip('.,;:-?"!')
            if lowercase:
                word = word.lower()
            unique_words[word] = 0
    return unique_words


def get_data(args: Iterable, flag_input: str, encoding: str) -> [str]:
    """Функция считывает данные в зависимости от настроек flag_input, encoding"""

    if flag_input == 'content':
        return args
    elif flag_input == 'filename':
        list_text = read_text_in_file(args, encoding)
        return list_text
    else:
        raise AttributeError('The input attribute does not have such an argument.')


def read_text_in_file(list_filename: Iterable, encoding_file: str) -> [str]:
    """Функция считывает данные из файлов"""

    list_text = []
    for filename in list_filename:
        with open(filename, encoding=encoding_file) as f:
            list_text.extend(f.readlines())
    return list_text


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
