import pytest

# Ejercicio 1

# Crea un conftest.py con una fixture llamada:

# numero()

# que retorne:

# 100

# Luego, en un archivo test_numero.py, crea un test que valide ese valor sin importar la fixture.

@pytest.fixture
def numero():

    return 100

# Ejercicio 2

# En conftest.py, crea una fixture:

# usuario()

# que retorne:

# {
#     "nombre": "Antonio",
#     "activo": True
# }

# En test_usuario.py, crea dos tests que validen el nombre y el estado.

@pytest.fixture
def usuario():

    return {
        "nombre": "Antonio",
        "activo": True
    }

# Ejercicio 3

# Crea una fixture compartida:

# clientes()

# que retorne:

# ["Ana", "Pedro", "Juan"]

# En otro archivo de test, verifica:

# Que la lista tenga 3 elementos.
# Que "Juan" exista.

@pytest.fixture
def clientes():

    return ["Ana", "Pedro", "Juan"]

# Ejercicio 4

# Crea una clase Usuario, una fixture que devuelva un objeto de esa clase y, desde un archivo distinto al conftest.py, valida sus atributos.

class User:

    def __init__(self):
        self.nombre = "Laura"
        self.edad = 25

@pytest.fixture
def user():

    return User()

# Ejercicio 5

# Crea una fixture response() que retorne:

# {
#     "status_code": 200,
#     "success": True,
#     "message": "OK"
# }

# En dos archivos de test diferentes, reutiliza la misma fixture para validar distintos campos.

@pytest.fixture
def response():

    return {
        "status_code": 200,
        "success": True,
        "message": "OK"
    }

# Desafío de entrevista (sin ejecutar)

# Responde:

# # conftest.py

# import pytest

# @pytest.fixture
# def numero():
#     print("Creando fixture")
#     return 10
# # test_numero.py

# def test_numero(numero):
#     print("Ejecutando test")
#     assert numero == 10
# ¿Qué se imprime primero? Creando fixture
# ¿Por qué test_numero() puede usar numero sin importarlo? debido a que numero() se encuentra dentro de conftest.py
# y se puede acceder desde cualquier lugar dentro del proyecto sin necesidad de importarlo
# ¿Qué archivo carga primero Pytest cuando encuentra una fixture compartida? conftest.py
# ¿Qué ventaja ofrece conftest.py frente a copiar la fixture en cada archivo de pruebas? nos permite reutilizar una fixture
# en varios tests definiendolo una sola vez y en caso de que necesitemos cambiar algun valor de dicha fixture para los tests
# del proyecto solo lo debemos de cambiar una sola vez en el fixture que se encuentra dentro de conftest.py