import unittest
from examen import CuentaBancaria, Persona, CajeroAutomático

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Juan")
        self.cuenta = CuentaBancaria(self.persona, saldo=1000)

    def test_consultar_saldo(self):
        self.assertEqual(self.cuenta.consultar_saldo(), 1000)

    def test_realizar_deposito(self):
        self.cuenta.realizar_deposito(500)
        self.assertEqual(self.cuenta.consultar_saldo(), 1500)

    def test_realizar_retiro_exitoso(self):
        self.cuenta.realizar_retiro(300)
        self.assertEqual(self.cuenta.consultar_saldo(), 700)

    def test_realizar_retiro_insuficiente(self):
        with self.assertRaises(ValueError):
            self.cuenta.realizar_retiro(2000)


class TestCajeroAutomático(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Juan")
        self.cuenta = CuentaBancaria(self.persona, saldo=1000)
        self.cajero = CajeroAutomático()

    def test_consultar_saldo(self):
        self.assertEqual(self.cajero.operar(self.cuenta, 'consultar'), 1000)

    def test_deposito(self):
        self.assertEqual(self.cajero.operar(self.cuenta, 'depositar', 500), 1500)

    def test_retiro_exitoso(self):
        self.assertEqual(self.cajero.operar(self.cuenta, 'retirar', 300), 700)

    def test_retiro_insuficiente(self):
        with self.assertRaises(ValueError):
            self.cajero.operar(self.cuenta, 'retirar', 2000)

if __name__ == '__main__':
    unittest.main()
