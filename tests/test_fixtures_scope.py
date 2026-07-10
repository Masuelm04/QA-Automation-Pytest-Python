import pytest

# Ejercicio 1

# Crea una fixture:

# @pytest.fixture(scope="function")

# que imprima:

# Creando número

# y retorne:

# 100

# Crea dos tests y observa que el mensaje aparece dos veces.

# @pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def numero():

    print("Creando número")

    return 100

def test_validar_numero_positivo(numero):

    assert numero > 0

def test_validar_numero_exacto(numero):

    assert numero == 100

# Ejercicio 2

# Cambia la misma fixture a:

# scope="module"

# Ejecuta los mismos dos tests.

# Pregunta: ¿Cuántas veces se imprime "Creando número"? una vez

# Ejercicio 3

# Crea una fixture:

# api_client()

# con:

# scope="session"

# que retorne un objeto sencillo:

# class ApiClient:
#     pass

# Haz tres tests distintos verificando:

# assert api_client is not None

class ApiClient:
    pass

@pytest.fixture(scope="session")
def api_client():

    return ApiClient()

def test_cliente_no_es_nulo(api_client):
    assert api_client is not None

def test_cliente_es_instancia_correcta(api_client):
   
    assert isinstance(api_client, ApiClient)

def test_cliente_mantiene_estado(api_client):
    
    assert api_client

# Ejercicio 4

# Crea una fixture:

# usuario()

# con:

# scope="function"

# que retorne:

# {
#     "nombre": "Antonio",
#     "activo": True
# }

# Haz tres tests distintos utilizando la misma fixture.

@pytest.fixture(scope="function")
def usuario():

    return {
        "nombre": "Antonio",
        "activo": True
    }

def test_verificar_estructura_diccionario(usuario):

    assert "nombre" in usuario
    assert "activo" in usuario

def test_verificar_nombre_usuario(usuario):

    assert usuario["nombre"] == "Antonio"

def test_verificar_usuario_activo(usuario):

    assert usuario["activo"] is True

# Ejercicio 5

# Imagina este código:

# @pytest.fixture(scope="session")
# def carrito():
#     return []

# Test 1:

# def test_agregar(carrito):
#     carrito.append("Laptop")

# Test 2:

# def test_carrito_vacio(carrito):
#     assert carrito == []

# Sin ejecutar:

# ¿Pasará el segundo test? No
# ¿Por qué? Porque el test valida que la lista este vacía y al momento de llegar a ejecutarse en este caso ya contiene el string Laptop,
# el cuál se conserva del test anterior, ya que el scope del fixture es session y dura para toda la session
# ¿Qué scope sería más apropiado? Sería más apropiado scope function
# ¿Qué principio de testing se está violando? el principio de aislamiento

# 🎯 Desafío de entrevista (Nivel QA Automation)

# Sin ejecutar:

# @pytest.fixture(scope="module")
# def usuario():
#     print("Creando usuario")
#     return {"nombre": "Antonio"}
# def test_1(usuario):
#     assert usuario["nombre"] == "Antonio"

# def test_2(usuario):
#     assert usuario is not None

# def test_3(usuario):
#     assert "nombre" in usuario

# Responde:

# ¿Cuántas veces se imprimirá "Creando usuario"? una vez
# ¿Por qué? Porque el scope del fixture es module, lo cual indica que se creará una sola vez para el modulo completo
# ¿Qué cambiaría si el scope fuera "function"? Se imprimiría "Creando usuario" tres veces, una por cada test
# ¿En qué situaciones reales usarías scope="module" en un framework de automatización? para test de una clase en especifico