import unittest
from Geometria_.model.Geometria import Geometria


class TestGeometria(unittest.TestCase):

    def setUp(self):
        self.shape = Geometria(10, 50, 4)

    def test_geometria(self):
        self.assertIsNotNone(self.shape)




if __name__ == '__main__':
    unittest.main()