import pytest

# Ejercicio 1

# Crea una fixture llamada:

# numero

# que retorne:

# 100

# Haz un test que valide ese valor.

@pytest.fixture
def numero():

    return 100

def test_validar_numero(numero):

    assert numero == 100

# Ejercicio 2

# Crea una fixture:

# usuario

# que retorne:

# {
#     "nombre":"Antonio",
#     "activo":True
# }

# Valida:

# nombre
# activo

@pytest.fixture
def usuario():

    return {
        "nombre": "Antonio",
        "activo": True
    }

def test_validar_nombre_usuario(usuario):

    assert usuario["nombre"] == "Antonio"

def test_validar_usuario_activo(usuario):

    assert usuario["activo"] == True

# Ejercicio 3

# Crea una fixture que retorne una lista:

# ["Ana","Pedro","Juan"]

# Valida:

# longitud
# que exista "Juan"

@pytest.fixture
def clientes():

    return [
        "Ana", "Pedro", "Juan"
    ]

def test_validar_longitud_lista(clientes):

    assert len(clientes) == 3

def test_validar_cliente(clientes):

    assert "Juan" in clientes

# Ejercicio 4

# Crea una clase:

# Usuario

# con:

# nombre
# edad

# Crea una fixture que retorne un objeto Usuario.

# Valida ambos atributos.

class User():

    def __init__(self):
        self.nombre = "Laura"
        self.edad = 25

@pytest.fixture
def user():

    return User()

def test_validar_nombre_user(user):

    assert user.nombre == "Laura"

def test_validar_edad_user(user):

    assert user.edad == 25

# Ejercicio 5

# Crea una fixture:

# response

# que retorne:

# {
#     "status_code":200,
#     "success":True
# }

# Haz dos pruebas utilizando la misma fixture.

@pytest.fixture
def response():

    return {
        "status_code": 200,
        "success": True
    }

def test_validar_status_code(response):

    assert response["status_code"] == 200

def test_validar_response_success(response):
    
    assert response["success"] == True

# Ejercicio 6

# Crea una fixture que retorne un objeto de tu clase ApiClient.

# Haz un test que solo verifique que el objeto fue creado correctamente usando:

# assert client is not None

class ApiClient():

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }
        self.timeout = 10

@pytest.fixture
def client():

    return ApiClient()

def test_validar_creacion_objeto_client(client):
    
    assert client is not None

# Ejercicio 7

# Crea una fixture que retorne una lista de diccionarios con usuarios.

# Haz un test que verifique que hay exactamente 2 usuarios activos.

@pytest.fixture
def users():

    return [
        {
            "nombre": "Antonia",
            "activo": True
        },
        {
            "nombre": "Maria",
            "activo": True
        }
    ]

def test_validar_users_activos(users):

    users_activos = [user for user in users if user.get("activo") == True]

    assert len(users_activos) == 2

# Ejercicio 8

# Crea una fixture con un diccionario que represente una respuesta de API.

# Haz tres tests distintos reutilizando esa misma fixture.

@pytest.fixture
def api_response():

    return {
        "status": 200,
        "message": "Registro de estudiante actualizado correctamente",
        "data": {
            "estudiante_id": "EST-001",
            "modulo": "Asistencia",
            "presente": True
        }
    }

def test_validar_status_response(api_response):

    assert api_response["status"] == 200

def test_validar_message_response(api_response):

    assert api_response["message"] == "Registro de estudiante actualizado correctamente"

def test_validar_estudiante_presente(api_response):

    assert api_response["data"]["presente"] == True

# Ejercicio 9

# Crea una fixture utilizando yield que imprima:

# Abriendo recurso

# antes del test y:

# Cerrando recurso

# después del test.

# Haz un test sencillo que use esa fixture para observar el orden de ejecución.

@pytest.fixture
def manejador_de_recurso():

    print("\nAbriendo recurso")

    yield

    print("\nCerrando recurso")

def test_observar_orden(manejador_de_recurso):

    print("\nEjecutando el test")

    assert True

# Ejercicio 10 (Nivel entrevista)

# Crea una fixture que devuelva un objeto Usuario y escribe tres tests independientes que validen diferentes atributos del mismo objeto. El objetivo es practicar la reutilización de fixtures para evitar crear el objeto manualmente en cada prueba.

class Colaborador:
    def __init__(self, nombre, rol, certificado):
        self.nombre = nombre
        self.rol = rol
        self.certificado = certificado
        self.activo = True 

@pytest.fixture
def colaborador_prueba():

    return Colaborador(nombre="Masuel", rol="QA Engineer", certificado=True)

def test_verificar_nombre_colaborador(colaborador_prueba):

    assert colaborador_prueba.nombre == "Masuel"

def test_verificar_rol_asignado(colaborador_prueba):

    assert colaborador_prueba.rol == "QA Engineer"

def test_verificar_estado_certificacion(colaborador_prueba):

    assert colaborador_prueba.certificado is True

# 🎯 Desafío de razonamiento (sin ejecutar)
# import pytest

# @pytest.fixture
# def numero():
#     print("Creando número")
#     return 10


# def test_numero(numero):
#     print("Ejecutando test")
#     assert numero == 10

# Responde:

# ¿Qué se imprime primero? Creando número
# ¿Por qué la fixture se ejecuta antes del test? Porque el test se ejecuta luego del return de la fixture
# ¿Qué ocurriría si el assert fallara? el test se marca como failed y se continue con los demás tests en caso de que existan
# ¿Se ejecuta igualmente el código de la fixture antes del fallo? Sí, porque el assert se ejecuta después de la ejecución del fixture