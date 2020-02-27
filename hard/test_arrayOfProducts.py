import unittest
from arrayOfProducts import arrayOfProducts

class arrayOfProductsTests(unittest.TestCase):
    def test_arrayOfProducts_Example(self):
        # Arrange
        inputArray = [1,2,3,4,5]
        expectedResult = [120,60,40,30,24]

        # Act
        actualResult = arrayOfProducts(inputArray)

        # Assert
        self.assertEqual(expectedResult, actualResult)