import unittest
from Geometria_.model.Geometria import Geometria
from random import randint
from Geometria_.view.View import View


class TestGeometria(unittest.TestCase):

    def setUp(self):
        """
        Creacion de instancias para las pruebas.
        """
        self.shapes = [
            Geometria(randint(2, 15), randint(2,15), randint(2, 15))
            for i in range(10)
        ]
        self.view = View()

    def test_geometria(self):
        """
        Subpruebas para cada figura
        """
        for shape in self.shapes:
            for i in range(1,9):
                with self.subTest():
                    self.assertIsNotNone(shape.switch(i))

    def test_view(self):
        for shape in self.shapes:
            self.assertIsNone(self.view.select(shape))

    def test_cuadrado(self):
        self.assertIsNotNone(self.shapes[0].switch(1))

    def test_circulo(self):
        self.assertIsNotNone(self.shapes[0].switch(2))

    def test_triangulo(self):
        self.assertIsNotNone(self.shapes[0].switch(3))

    def test_rectangulo(self):
        self.assertIsNotNone(self.shapes[0].switch(4))

    def test_pentagono(self):
        self.assertIsNotNone(self.shapes[0].switch(5))

    def test_rombo(self):
        self.assertIsNotNone(self.shapes[0].switch(6))

    def test_romboide(self):
        self.assertIsNotNone(self.shapes[0].switch(7))

    def test_trapecio(self):
        self.assertIsNotNone(self.shapes[0].switch(8))


if __name__ == '__main__':
    unittest.main()