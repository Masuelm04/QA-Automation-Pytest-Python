from unittest.mock import patch

# Ejercicio 1 - Mockear una función
# Objetivo

# Aprender a usar patch sobre una función y modificar su return_value.

def obtener_impuesto():
    return 18


def calcular_total(precio):
    impuesto = obtener_impuesto()
    return precio + impuesto
# Lo que debes hacer

# Escribe un test que:

# Mockee obtener_impuesto().
# Haga que retorne 30.
# Verifique que:
# calcular_total(100)

# devuelve

# 130

def test_calcular_total():
    with patch("learning_exercises.tests.test_patch.obtener_impuesto") as mock_obtener_impuesto:
        mock_obtener_impuesto.return_value = 30

        resultado = calcular_total(100)

        assert resultado == 130

# Ejercicio 2 - Mockear un método de una clase
# Objetivo

# Aprender cómo funciona Mock.return_value.

class Inventario:

    def hay_stock(self, producto):
        return True


def procesar_compra(producto):

    inventario = Inventario()

    if inventario.hay_stock(producto):
        return "Compra realizada"

    return "Sin inventario"
# Lo que debes hacer

# Escribe dos pruebas.

# Prueba 1

# Mockea la clase para que

# hay_stock()

# devuelva

# True

# y verifica

# "Compra realizada"

# Prueba 2

# Haz que devuelva

# False

# y verifica

# "Sin inventario"

def test_procesar_compra_con_stock():
    with patch("learning_exercises.tests.test_patch.Inventario") as MockInventario:
        mock_inventario = MockInventario.return_value
        mock_inventario.hay_stock.return_value = True

        resultado = procesar_compra("producto")

        assert resultado == "Compra realizada"

def test_procesar_compra_sin_stock():
    with patch("learning_exercises.tests.test_patch.Inventario") as MockInventario:
        mock_inventario = MockInventario.return_value
        mock_inventario.hay_stock.return_value = False

        resultado = procesar_compra("producto")

        assert resultado == "Sin inventario"