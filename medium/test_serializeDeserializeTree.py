import unittest
from serializeDeserializeTree import Node
from serializeDeserializeTree import serialize


class SerializeDeserializeTreeTests(unittest.TestCase):
    def test_serializeDeserializeTree_Example(self):
        # Arrange
        inputNode = Node('root', Node('left', Node('left.left')), Node('right'))

        expectedResult = 'root(left(left.left()())())(right()())'

        # Act
        actualResult = serialize(inputNode)

        # Assert
        self.assertEqual(expectedResult, actualResult)