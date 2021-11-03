import unittest
from Geometria_.model.Geometria import Geometria


class TestGeometria(unittest.TestCase):

    def setUp(self):
        self.shape = Geometria(10, 50, 4)

    def test_geometria(self):
        # self.assertIsNotNone(self.shape)
        for i in range(1,9):
            with self.subTest():
                self.assertIsNotNone(self.shape.switch(i))






if __name__ == '__main__':
    unittest.main()