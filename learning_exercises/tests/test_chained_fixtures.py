import pytest
from test_mark_parametrize import ApiClient

# Ejercicio 1

# Crear:

# usuario()

# Retorna:

# {
#     "nombre":"Antonio"
# }

# Crear:

# usuario_activo(usuario)

# Agregar:

# "activo": True

# Validar.

@pytest.fixture
def usuario():

    return {
        "nombre": "Antonio"
    }

@pytest.fixture()
def usuario_activo(usuario):

    usuario["activo"] = True

    return usuario

def test_validar_usuario(usuario_activo):

    assert usuario_activo["nombre"] == "Antonio"
    assert usuario_activo["activo"] is True

# Ejercicio 2

# Crear fixtures dependientes:

# token()

# ↓

# headers(token)

# Validar Authorization.

@pytest.fixture
def token():

    return "abc1234"

@pytest.fixture
def headers(token):

    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

def test_validar_authorization(headers):

    assert "Authorization" in headers

    assert headers["Authorization"] == "Bearer abc1234"

# Ejercicio 3

# Clase:

# User

# Fixture:

# user()

# Validar atributos.

class User:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

@pytest.fixture
def user():

    return User("Antonio", 22)

def test_validar_nombre_usuario(user):

    assert user.nombre == "Antonio"

def test_validar_edad_usuario(user):

    assert user.edad == 22

# Ejercicio 4

# Crear fixture factory:

# crear_usuario()

# Generar:

# Ana
# Pedro
# Maria

@pytest.fixture
def crear_usuario():

    def _crear(nombre, edad):

        return User(nombre, edad)
    
    return _crear

def test_usuario(crear_usuario):

    usuario = crear_usuario("Ana", 30)

    assert usuario.nombre == "Ana"

def test_usuario_1(crear_usuario):

    usuario_1 = crear_usuario("Pedro", 20)

    assert usuario_1.nombre == "Pedro"

def test_usuario_2(crear_usuario):

    usuario_2 = crear_usuario("Maria", 19)

    assert usuario_2.nombre == "Maria"

# Ejercicio 5

# Fixture con yield:

# Abrir conexión

# ↓

# test

# ↓

# Cerrar conexión

@pytest.fixture
def conexion():

    print("Abrir conexión")

    yield

    print("Cerrar conexión")

@pytest.fixture
def cliente(conexion):

    print("Creando cliente")

    yield {
        "nombre": "Luis"
    }

    print("Eliminando cliente")

def test_cliente(cliente):

    assert cliente["nombre"] == "Luis"

# Ejercicio (Nivel entrevista)

# Explicar sin ejecutar:

# @pytest.fixture
# def token():

#     print("token")

#     yield "abc"

#     print("cleanup token")


# @pytest.fixture
# def headers(token):

#     print("headers")

#     return {
#         "Authorization": token
#     }


# def test_api(headers):

#     print("test")

# Responder:

# ¿Qué se imprime primero? token
# ¿Qué se imprime después? headers
# ¿Se ejecuta cleanup token? Si
# ¿Por qué? Porque la fixture token() utiliza la palabra clave yield en lugar de return.
#   Las fixtures que utilizan yield ejecutan el código anterior al yield durante la fase de setup. 
#   Una vez finaliza el test, Pytest continúa ejecutando el código posterior al yield, realizando automáticamente el teardown o cleanup
# ¿Qué dependencia existe entre las fixtures?
#   headers depende directamente de token.
#   test_api depende de headers e indirectamente de token.