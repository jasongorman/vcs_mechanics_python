import unittest

from src.fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_first_number_is_zero(self):
        self.assertEqual(0, fibonacci(0))

    def test_second_number_is_one(self):
        self.assertEqual(1, fibonacci(1))

    def test_third_number_is_one(self):
        self.assertEqual(1, fibonacci(2))

    def test_fourth_number_is_two(self):
        self.assertEqual(2, fibonacci(3))

    def test_fifth_number_is_three(self):
        self.assertEqual(3, fibonacci(4))


if __name__ == '__main__':
    unittest.main()
