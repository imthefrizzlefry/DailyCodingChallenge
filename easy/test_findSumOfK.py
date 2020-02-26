import unittest
from findSumOfK import FindSumOfK

class findSumOfKTests(unittest.TestCase):
    def test_findSumOfTests_ProvidedExample(self):
        s = [10, 15, 3, 7]
        k = 17

        self.assertTrue(FindSumOfK(s, k))