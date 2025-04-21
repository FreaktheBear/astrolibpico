import unittest
import calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        # Set up any necessary data or state before each test
        self.a = 5
        self.b = 3

    def test_add(self):
        # Test the add function with known values
        result = calc.add(self.a, self.b)
        self.assertEqual(result, 8)

    def test_subtract(self):
        # Test the subtract function with known values
        result = calc.subtract(self.a, self.b)
        self.assertEqual(result, 2)

    def test_multiply(self):
        # Test the multiply function with known values
        result = calc.multiply(self.a, self.b)
        self.assertEqual(result, 15)

    def test_divide(self):
        # Test the divide function with known values
        result = calc.divide(self.a, self.b)
        self.assertEqual(result, 1.6666666666666667)

if __name__ == '__main__':
    unittest.main()
