import unittest
import calculatemeal

class TestCalculateMeal(unittest.TestCase):
    """docstring for [object Object]."""
    def test_total(self):
        result=200.00+(200.00*0.0875)+(217.50*0.2)
        self.assertEqual(result,261)
        
