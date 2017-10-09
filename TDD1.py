import unittest
import CalculatorFunctions

class KnownValues(unittest.TestCase):
    #formula for unittest method name is...
    #test_functionName_testDescription
    def test_caculateBMI_forLowerBoundary(selfself):
        result = CalculatorFunctions.calculateBMI(58, 91)
        expected = 19
        self.assertEqual(expected, result)

if__name__=='main':
    unittest