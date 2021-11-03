import unittest
from Geometria_.model.Geometria import Geometria
from random import randint
from Geometria_.view.View import View


class TestGeometria(unittest.TestCase):

    def setUp(self):
        self.shapes = [
            Geometria(randint(2, 15), randint(2,15), randint(2, 15))
            for i in range(10)
        ]
        self.view = View()

    def test_geometria(self):
        for shape in self.shapes:
            for i in range(1,9):
                with self.subTest():
                    self.assertIsNotNone(shape.switch(i))

    def test_view(self):
        for shape in self.shapes:
            self.assertIsNone(self.view.select(shape))
            # self.assert_(self.view.select(shape))


if __name__ == '__main__':
    unittest.main()