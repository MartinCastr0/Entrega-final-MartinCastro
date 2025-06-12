from django.test import TestCase
from .models import Entrada

class EntradaModelTest(TestCase):
    def test_str(self):
        entrada = Entrada(titulo="Test", contenido="Contenido de prueba")
        self.assertEqual(str(entrada), "Test")