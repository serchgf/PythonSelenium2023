"""
Crea un archivo llamado test_cuenta_bancaria.py y agrega la clase de
CuentaBancaria
2. Crea una clase de prueba llamada TestCuentaBancaria.
3. Dentro de la clase de prueba, crea dos métodos: setup_method y
teardown_method.
4. En el método setup_method, crea una nueva instancia de la clase
CuentaBancaria y guárdala en una variable de instancia.
5. En el método teardown_method, no es necesario hacer nada, ya que no hay
nada que limpiar después de cada prueba.
6. Define tres métodos de prueba: test_depositar, test_retirar y
test_retirar_insuficiente.
7. En cada método de prueba, utiliza la instancia de la cuenta de prueba creada
en el método setup_method.
8. En cada método de prueba, utiliza las aserciones de pytest para verificar que
las operaciones de depósito y retiro se realizan correctamente y que se lanza
una excepción si se intenta retirar más de lo que hay en la cuenta.
9. Ejecuta las pruebas utilizando pytest y verifica que todas las pruebas pasen
correctamente.
"""

class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo

class TestCuentaBancaria:

    def setup_method(self):
        self.cuenta_bancaria = CuentaBancaria("Jaime Maussan", 10)

    def test_depositar(self):
        print(f"\n_____________Test Depositar")
        saldo_disponible = self.cuenta_bancaria.consultar_saldo()
        print(f"\nsaldo disponible es: {saldo_disponible}")
        cantidad = 10
        self.cuenta_bancaria.depositar(cantidad)
        saldo = self.cuenta_bancaria.consultar_saldo()
        print(f"depositaste: {cantidad}\nel nuevo saldo es: {saldo}")
        assert saldo == 20, "el saldo deberia ser 20"

    def test_depositar_cantidad_negativa(self):
        print(f"\n_____________Test Depositar cantidad negativa")
        saldo_disponible = self.cuenta_bancaria.consultar_saldo()
        print(f"\nsaldo disponible es: {saldo_disponible}")
        cantidad = -10
        self.cuenta_bancaria.depositar(cantidad)
        saldo = self.cuenta_bancaria.consultar_saldo()
        print(f"depositaste: {cantidad}\nel nuevo saldo es: {saldo}")
        assert saldo == 10, "el saldo 10 no deberia cambiar, operacion no permitida con cantides de deposito negativos"

    def test_retirar(self):
        print(f"\n_____________Test Retirar Con saldo suficiente")
        saldo_disponible = self.cuenta_bancaria.consultar_saldo()
        print(f"\nsaldo disponible es: {saldo_disponible}")
        cantidad = 5
        self.cuenta_bancaria.retirar(cantidad)
        saldo = self.cuenta_bancaria.consultar_saldo()
        print(f"Retiraste: {cantidad}")
        assert saldo == 5, "el saldo deberia ser 5"

    def test_retirar_flotante(self):
        print(f"\n_____________Test Retirar Con cantidad")
        saldo_disponible = self.cuenta_bancaria.consultar_saldo()
        print(f"\nsaldo disponible es: {saldo_disponible}")
        cantidad = 5.35
        self.cuenta_bancaria.retirar(cantidad)
        saldo = self.cuenta_bancaria.consultar_saldo()
        print(f"Retiraste: {cantidad}")
        assert saldo == 5, "el saldo debe ser 5, no deberia permitir cantidades no enteras"

    def test_retirar_cantidad_negativa(self):
        print(f"\n_____________Test Retirar Con cantidad negativa")
        saldo_disponible = self.cuenta_bancaria.consultar_saldo()
        print(f"\nsaldo disponible es: {saldo_disponible}")
        cantidad = -5
        self.cuenta_bancaria.retirar(cantidad)
        saldo = self.cuenta_bancaria.consultar_saldo()
        print(f"Retiraste: {cantidad}")
        assert saldo == 10, "el saldo deberia ser 10 porque una cantidad negativa no deberia ser valida ni permitida"


    def test_retirar_insuficiente(self):
        print(f"\n_____________Test Retirar Con saldo insuficiente")
        saldo_disponible = self.cuenta_bancaria.consultar_saldo()
        print(f"\nEl saldo disponible es: {saldo_disponible}")
        cantidad = 15
        print(f"quieres Retirar: {cantidad}")
        self.cuenta_bancaria.retirar(cantidad)

    def teardown_method(self):
        print("No hay que hacer nada")