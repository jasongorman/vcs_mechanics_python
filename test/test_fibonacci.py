import unittest

from src.fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_first_number_is_zero(self):
        self.assertEqual(0, fibonacci(0))

    def test_first_number_is_zero(self):
        self.assertEqual(1, fibonacci(1))


if __name__ == '__main__':
    unittest.main()
