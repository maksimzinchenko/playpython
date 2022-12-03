import unittest
from parse_matrix.parse_matrix import parse_matrix

INPUT1 = '''
        +-----+-----+-----+-----+
        |  10 |  20 |  30 |  40 |
        +-----+-----+-----+-----+
        |  50 |  60 |  70 |  80 |
        +-----+-----+-----+-----+
        |  90 | 100 | 110 | 120 |
        +-----+-----+-----+-----+
        | 130 | 140 | 150 | 160 |
        +-----+-----+-----+-----+
        '''

INPUT2 = '''
        +-----+-----+-----+-----+
        |  10 |  20 |  30 |  40 |
        +-----+-----+-----+-----+
        |  50 |  60 |  70 |  80 |
        +-----+-----+-----+-----+
        |  90 | 100 | 110 | 120 |
        +-----+-----+-----+-----+
        | 130 | 140 | 150 | 160
        '''

MATRIX = [
    10, 20, 30, 40,
    50, 60, 70, 80,
    90, 100, 110, 120,
    130, 140, 150, 160,
]

class TestMatrixParsing(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(parse_matrix(INPUT1), MATRIX)

    def test_finished_with_digit(self):
        self.assertEqual(parse_matrix(INPUT2), MATRIX)

if __name__ == '__main__':
    unittest.main()