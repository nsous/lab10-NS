#https://github.com/nsous/lab10-NS
#Partner 1: Nicole Sous
#Partner 2: NA
#I did both roles, as per Case's recommendation because my group partner did not answer me.

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(7,3),10)
        self.assertEqual(add(6,5),11)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(7,6), 1)
        self.assertEqual(subtract(9,2),7)
        self.assertEqual(subtract(5,1),4)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(4,2),8)
        self.assertEqual(multiply(7,8),56)
        self.assertEqual(multiply(3,2), 6)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(8,2),4)
        self.assertEqual(divide(18,2),9)
        self.assertEqual(divide(9,3),3)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(25,5),2)
        self.assertEqual(logarithm(35,2),5)
        self.assertEqual(logarithm(27,3),3)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,6)



    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 4)



    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(2,3),6)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(4,3),5)



    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        with self.assertRaises(ValueError):
            square_root(-25)
        with self.assertRaises(ValueError):
            square_root(-16)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()