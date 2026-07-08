import pytest

# Ejercicio 1

# Crea un test parametrizado que reciba los números:

# 1
# 5
# 10
# 20

# Valida que todos sean mayores que cero.

@pytest.mark.parametrize(
    "numeros",
    [1, 5, 10, 20]
)

def test_validar_numeros_mayores_a_cero(numeros):

    assert numeros > 0

# Ejercicio 2

# Parametriza tres pares de números:

# (2,3,5)
# (10,5,15)
# (8,12,20)

# Valida que la suma sea correcta.

@pytest.mark.parametrize(
    "a, b, resultado",
    [
        (2, 3, 5),
        (10, 5, 15),
        (8, 12, 20)
    ]
)

def test_validar_suma_numeros(a, b, resultado):

    assert a + b == resultado

# Ejercicio 3

# Parametriza los siguientes nombres:

# Ana
# Pedro
# Juan
# Maria

# Valida que todos tengan una longitud mayor que 2.

@pytest.mark.parametrize(
    "nombres",
    ["Ana", "Pedro", "Juan", "Maria"]
)

def test_validar_longitud_nombres(nombres):

    assert len(nombres) > 2

# Ejercicio 4

# Parametriza los siguientes status:

# 200
# 201
# 204
# 404
# 500

# Valida si pertenecen al conjunto de respuestas exitosas (200, 201, 204).

# Puedes incluir un segundo parámetro esperado (True/False) para comprobar el resultado.

@pytest.mark.parametrize(
    "status, esperado",
    [
        (200, True),
        (201, True),
        (204, True),
        (404, False),
        (500, False)
    ]
)

def test_validar_status_exitosos(status, esperado):

    assert (status in [200, 201, 204]) == esperado

# Ejercicio 5

# Crea una clase:

# class Usuario:

# con un atributo nombre.

# Parametriza tres nombres distintos y verifica que el objeto almacene correctamente el nombre recibido.

class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre

@pytest.mark.parametrize(
    "nombres",
    ["Laura", "Marcos", "Patricia"]
)

def test_validar_nombres_usuario(nombres):

    usuario = Usuario(nombres)

    assert usuario is not None