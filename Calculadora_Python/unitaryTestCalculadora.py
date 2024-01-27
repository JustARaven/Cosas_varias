# Test Unitario
import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 4), 8)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 0), "No puedes dividir entre cero, vuelve a intentarlo.")

if __name__ == '__main__':
    # Cargar las pruebas desde el TestCalculadora
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)

    # Crear un corredor de pruebas y ejecutar las pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Imprimir el resultado en función del éxito o fracaso
    if result.wasSuccessful():
        print("\n¡Todas las pruebas pasaron exitosamente!")
    else:
        print("\nAlgunas pruebas fallaron. Detalles:")

        for failure in result.failures:
            test_name = failure[0].id().split('.')[-1]
            print(f"\nPrueba fallida: {test_name}")
            print(f"Detalle del fallo:\n{failure[1]}")
