import unittest
import addnumbers

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        result=addnumbers.add(30,40)
        self.assertEqual(result,70)
