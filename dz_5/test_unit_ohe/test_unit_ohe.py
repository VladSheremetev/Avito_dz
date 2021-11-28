import unittest
from ohe import fit_transform


class TestTF(unittest.TestCase):
    def test_fit_transform_0(self):
        data = []
        exp_transformed = []
        self.assertEqual(fit_transform(data), exp_transformed)

    def test_fit_transform_1(self):
        data = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(data), exp_transformed)

    def test_fit_transform_2(self):
        data = [1]
        exp_transformed = [
            (1, [1]),
        ]
        self.assertEqual(fit_transform(data), exp_transformed)

    def test_fit_transform_3(self):
        data = [1, '', ['c']]
        with self.assertRaises(TypeError):
            fit_transform(data)

    def test_fit_transform_4(self):
        data = [1]
        exp_transformed = [
            (1, [1]),
        ]
        self.assertIsInstance(fit_transform(data), type(exp_transformed))

    def test_fit_transform_error(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
