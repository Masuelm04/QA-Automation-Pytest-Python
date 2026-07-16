# Ejercicio 1

# Importa:

# from unittest.mock import Mock

# Crea un objeto:

# usuario = Mock()

# Asígnale:

# usuario.nombre = "Antonio"

# Imprime:

# usuario.nombre

from unittest.mock import Mock

usuario = Mock()

usuario.nombre = "Antonio"

print(usuario.nombre)

# Ejercicio 2

# Crea un Mock llamado:

# api

# Agrega un método:

# obtener_status()

# que retorne:

# 200

# Utiliza:

# return_value

api = Mock()

api.obtener_status.return_value(200)

# Ejercicio 3

# Crea un Mock llamado:

# cliente

# Agrega:

# cliente.nombre = "Ana"
# cliente.edad = 25

# Valida ambos atributos usando assert.

cliente = Mock()

cliente.nombre = "Ana"
cliente.edad = 25

def test_validar_cliente():

    assert cliente.nombre == "Ana"
    assert cliente.edad == 25

# Ejercicio 4

# Simula un método:

# login()

# que retorne:

# True

# Verifica el resultado.

auth = Mock()

auth.login.return_value = True

resultado = auth.login()

def test_validar_login():

    assert resultado is True

# Ejercicio 5

# Llama un método:

# guardar()

# y verifica que fue llamado utilizando:

# assert_called_once()

articulo = Mock()

articulo.guardar.return_value = {
    "id": 1,
    "nombre_articulo": "Smartphone"
}

guardados = articulo.guardar()

def test_validar_articulos_guardados():

    assert guardados["nombre_articulo"] == "Smartphone"

    articulo.guardar.assert_called_once()