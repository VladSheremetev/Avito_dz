import typing as t
import math


def tf_transform(count_matrix: t.List[t.List[int]]) -> t.List[int]:
    tf_matrix = []

    for vec in count_matrix:
        number_of_word = sum(vec)
        tf_matrix_row = [round(i / number_of_word, 3) for i in vec]
        tf_matrix.append(tf_matrix_row)

    return tf_matrix


def idf_transform(count_matrix: t.List[t.List[int]]) -> t.List[int]:
    result = list()
    document_count = len(count_matrix) + 1

    for col in range(len(count_matrix[0])):
        cur_sum = 0
        for row in range(len(count_matrix)):
            cur_sum += bool(count_matrix[row][col])
        result.append(cur_sum + 1)

    for i in range(len(result)):
        result[i] = round(math.log(document_count / result[i]) + 1, 1)

    return result


class TfidfTransformer:
    def fit_transform(self, matrix):
        tf = tf_transform(matrix)
        idf = idf_transform(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])

        return tf_idf


class CountVectorizer:
    def __init__(self):
        self._unique_words = []
        self._count_word_in_text = []

    def fit_transform(self, list_text: t.List[str]):
        self._unique_words, self._count_word_in_text = self.count_words_in_list_text(list_text)
        return self._count_word_in_text

    def get_feature_names(self):
        return self._unique_words

    @staticmethod
    def count_words_in_list_text(list_text: t.Iterable) -> t.Tuple[t.List[str], t.List[str]]:
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


def zero_values(dict_words: t.Dict[str, int]) -> None:
    """Функция, которая обнуляет счётчик слов"""
    for key in dict_words.keys():
        dict_words[key] = 0


def get_unique_words_in_list_text(list_text: t.List[str]) -> t.Dict[str, int]:
    """Функция, которая создаёт словарь со всеми уникальными словами во всех последовательностях текстов\
    в качестве ключей, а счётчик слов в качестве values
    """
    unique_words = {}
    for text in list_text:
        for word in text.split():
            word = word.strip('.,;:-?"!').lower()
            unique_words[word] = 0
    return unique_words


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)

    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)

    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
