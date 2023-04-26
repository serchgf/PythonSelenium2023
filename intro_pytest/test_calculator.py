"""
1. Crea un archivo llamado "test_calculator.py".
2. Importa la biblioteca pytest al principio del archivo.
3. Crea una función llamada "test_suma" que use la función suma de la
calculadora para sumar dos números y verificar que el resultado es correcto
utilizando la aserción assert.
4. Crea otra función llamada "test_resta" que use la función resta de la
calculadora para restar dos números y verificar que el resultado es correcto
utilizando la aserción assert.
5. Crea una tercera función llamada "test_multiplicacion" que use la función
multiplicación de la calculadora para multiplicar dos números y verificar que
el resultado es correcto utilizando la aserción assert.
6. Crea una cuarta función llamada "test_division" que use la función división de
la calculadora para dividir dos números y verificar que el resultado es correcto
utilizando la aserción assert.
7. Ejecuta el archivo

"""

import pytest


class Calculadora:

    def __init__(self):
       pass

    def suma(self, num_a: int, num_b: int):
       return num_a + num_b

    def resta(self, num_a: int, num_b: int):
       return num_a - num_b

    def multiplicacion(self, num_a: int, num_b: int):
       return num_a * num_b

    def division(self, num_a: int, num_b: int):
       return num_a // num_b

def test_suma():
    calc = Calculadora()
    result = calc.suma(2,3)
    assert result == 5, "El resultado de sumar '2' + '3' deberia ser '5'"

def test_resta():
    calc = Calculadora()
    result = calc.resta(2,3)
    assert result == -1, "El resultado de restar '2' - '3' deberia ser '-1'"

def test_multiplicacion():
    calc = Calculadora()
    result = calc.multiplicacion(2,3)
    assert result == 6, "El resultado de multiplicar '2' * '3' deberia ser '6'"

def test_division():
    calc = Calculadora()
    result = calc.division(12,3)
    assert result == 4, "El resultado de dividir '9' + '3' deberia ser '4'"