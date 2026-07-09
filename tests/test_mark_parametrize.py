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

    assert usuario.nombre == nombres

# Ejercicio 6

# Crea una fixture que retorne un objeto ApiClient (puede ser una versión sencilla).

# Parametriza los endpoints:

# "/users/1"
# "/users/2"
# "/users/3"

# En el test no hace falta realizar llamadas HTTP; simplemente verifica que el objeto exista (assert api_client is not None) y que el endpoint recibido empiece por /

class ApiClient():

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }
        self.timeout = 10

@pytest.fixture
def api_client():

    return ApiClient()

def test_validar_existencia_objeto(api_client):

    assert api_client is not None

@pytest.mark.parametrize(
    "endpoint",
    ["/users/1", "/users/2", "/users/3"]
)

def test_validar_inicio_endpoint(endpoint):

    assert endpoint.startswith("/")

# Ejercicio 7

# Parametriza una lista de usuarios con su estado esperado:

# ("Ana", True)
# ("Pedro", False)
# ("Juan", True)

# Valida que el estado recibido coincida con el esperado.

def obtener_estado_usuario(usuario):

    user = {
        "Ana": True,
        "Pedro": False,
        "Juan": True
    }

    return user.get(usuario)

@pytest.mark.parametrize(
    "usuario, esperado",
    [
        ("Ana", True),
        ("Pedro", False),
        ("Juan", True)
    ]
)

def test_validar_estado_usuario(usuario, esperado):

    recibido = obtener_estado_usuario(usuario)

    assert recibido == esperado

# Ejercicio 8

# Parametriza distintos diccionarios que representen respuestas de API:

# {"status":200}
# {"status":404}
# {"status":500}

# Valida que cada uno tenga la clave "status".

@pytest.mark.parametrize(
    "respuesta_api",
    [
        {"status": 200},
        {"status": 404},
        {"status": 500}
    ]
)

def test_validar_clave_status(respuesta_api):

    assert "status" in respuesta_api

# Ejercicio 9

# Combina una fixture que retorne un diccionario base con un test parametrizado que reciba distintas claves ("id", "name", "email"). Valida que todas existan en el diccionario.

@pytest.fixture
def empleado():

    return {
        "id": 1,
        "name": "Lucas",
        "email": "lucas@gmail.com"
    }

@pytest.mark.parametrize(
    "clave",
    ["id", "name", "email"]
)

def test_validar_claves_json_empleado(clave, empleado):

    assert clave in empleado

# Ejercicio 10 (Nivel entrevista)

# Combina:

# una fixture que cree un objeto Usuario,
# un test parametrizado con distintos atributos ("nombre", "edad"),

# y valida dinámicamente que esos atributos existan usando hasattr().

class Usuario_n:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

@pytest.fixture
def usuario_test():

    return Usuario_n("Carlos", 50)

@pytest.mark.parametrize(
    "atributo",
    ["nombre", "edad"]
)

def test_validar_existencia_atributos_usuario(usuario_test, atributo):

    assert hasattr(usuario_test, atributo)

# 🎯 Desafío de razonamiento (sin ejecutar)
# import pytest

# @pytest.mark.parametrize(
#     "numero",
#     [1, 2, 3]
# )
# def test_numero(numero):

#     print(f"Probando {numero}")

#     assert numero < 3

# Responde:

# ¿Cuántas veces ejecutará Pytest este test? 3 veces
# ¿Qué casos pasarán y cuál fallará? Pasarán los casos con los valores de numero 1 y 2; fallará el caso con numero con valor 3
# ¿Se dejarán de ejecutar los demás casos al fallar uno? No
# ¿Qué ventaja tiene esto frente a escribir tres funciones de test separadas? Reduce tiempo, además sirve para marcar los que pasan y los que noy cada caso aparece como una prueba independiente en el reporte de Pytest.