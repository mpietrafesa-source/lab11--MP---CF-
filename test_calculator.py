import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,3), 8)
        self.assertEqual(add(-2, 3), 1)
        

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(4,-3), 7)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 3), -6)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(4, 20), 5)
        self.assertEqual(calculator.div(3, 0), 0)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEquals(log(2, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
            with self.assertRaises(ValueError):
                log(2, 0)
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(2, -5)

        with self.assertRaises(ValueError):
            calculator.log(0, 10)
    
    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
        self.assertEqual(calculator.hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(25), 5)
        self.assertEqual(calculator.square_root(0), 0)

        with self.assertRaises(ValueError):
            calculator.square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
