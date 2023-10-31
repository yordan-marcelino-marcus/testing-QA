import fibonacci
import unittest

class TestFibonacci(unittest.TestCase):

    def test_validate_number_for_fibonacci_with_non_integer_input(self):
        try:
            fibonacci.validate_number_for_fibonacci("hello")
        except TypeError as e:
            self.assertEqual(str(e),"Input must be an integer")

    def test_validate_number_for_fibonacci_with_negative_input(self):
        try:
            fibonacci.validate_number_for_fibonacci(-1)
        except ValueError as e:
            self.assertEqual(str(e),"Input must be a positive integer")

    def test_fibonacci_with_non_integer_input(self):
        try:
            fibonacci.fibonacci("hello")
        except TypeError as e:
            self.assertEqual(str(e),"Input must be an integer")

    def test_fibonacci_with_negative_input(self):
        try:
            fibonacci.fibonacci(-1)
        except ValueError as e:
            self.assertEqual(str(e),"Input must be a positive integer")

    def test_fibonacci(self):
        self.assertEqual(fibonacci.fibonacci(1), 0)
        self.assertEqual(fibonacci.fibonacci(2), 1)
        self.assertEqual(fibonacci.fibonacci(3), 1)
        self.assertEqual(fibonacci.fibonacci(4), 2)
        self.assertEqual(fibonacci.fibonacci(5), 3)
        self.assertEqual(fibonacci.fibonacci(6), 5)

class TestValidator(unittest.TestCase):

    def test_validate_number_for_fibonacci_with_non_integer_input(self):
        try:
            fibonacci.validate_number_for_fibonacci("hello")
        except TypeError as e:
            self.assertEqual(str(e),"Input must be an integer")

    def test_validate_number_for_fibonacci_with_negative_input(self):
        try:
            fibonacci.validate_number_for_fibonacci(-1)
        except ValueError as e:
            self.assertEqual(str(e),"Input must be a positive integer")

    def test_validate_number_for_fibonacci_with_correct_input(self):
        fibonacci.validate_number_for_fibonacci(1)

class TestFibonacciArray(unittest.TestCase):

    def test_fibonacci_array_with_non_integer_input(self):
        try:
            fibonacci.fibonacci_array("hello",1)
        except TypeError as e:
            self.assertEqual(str(e),"Input must be an integer")
        try:
            fibonacci.fibonacci_array(1,"hello")
        except TypeError as e:
            self.assertEqual(str(e),"Input must be an integer")
        try:
            fibonacci.fibonacci_array("hello","hello")
        except TypeError as e:
            self.assertEqual(str(e),"Input must be an integer")

    def test_fibonacci_array_with_negative_input(self):
        try:
            fibonacci.fibonacci_array(-1,1)
        except ValueError as e:
            self.assertEqual(str(e),"Input must be a positive integer")
        try:
            fibonacci.fibonacci_array(1,-1)
        except ValueError as e:
            self.assertEqual(str(e),"Input must be a positive integer")
        try:
            fibonacci.fibonacci_array(-1,0)
        except ValueError as e:
            self.assertEqual(str(e),"Input must be a positive integer")

    def test_fibonacci_array(self):
        self.assertEqual(fibonacci.fibonacci_array(1,2),[0, 1])
        self.assertEqual(fibonacci.fibonacci_array(1,8),[0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci.fibonacci_array(5,7),[3, 5, 8])

if __name__ == '__main__':
    unittest.main()