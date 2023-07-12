import unittest
from unittest.mock import Mock

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


class TestFileIO(unittest.TestCase):
    """A test class to test file IO"""

    def test_import(self):
        """A test case to test importing a .json file"""
        pass

    def test_export(self):
        """A test case to test exporting a .json file"""
        #self.assertRaises(ZeroDivisionError, div, 1,0)
        pass

    def test_open(self):
        """A test case to test opening a .json file"""
        pass

class TestCalculation(unittest.TestCase):
    """A test class to test the calculation"""

    def test_total(self):
        """A test case to check if the calculation is correct"""
        pass

if __name__ == '__main__':
    unittest.main()

